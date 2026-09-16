# Technical Deep Dives + Likely Q&A (per JD keyword)

Study in this priority order for a 2-day sprint:
**1) Apache Iceberg  2) Glue/Athena/S3/Lake Formation  3) dbt  4) Airflow/Step Functions  5) PySpark  6) Data quality/observability**

---

## 1. Apache Iceberg (HIGHEST PRIORITY — "preferred" and named twice)

**What it is (one-liner):** An open **table format** for huge analytic datasets on object
storage (S3). It adds a metadata layer over data files (Parquet/ORC) giving you ACID
transactions, schema evolution, hidden partitioning, and time travel — turning a "folder of
files in S3" into a real table.

**How it works (know this cold):**
- Layers: **catalog** → points to current **metadata file** (table state, schema, snapshots)
  → **manifest list** → **manifest files** (list data files + stats) → **data files** (Parquet).
- A write creates a **new snapshot** (metadata file); readers see a consistent snapshot →
  **serializable isolation / ACID** without locking the whole table.

**Key features to name:**
- **Schema evolution:** add/drop/rename/reorder columns safely — columns tracked by **unique ID**,
  not by name/position, so no data rewrite and no "wrong column" bugs. (JD: "schema evolution".)
- **Hidden partitioning:** you partition by a transform (e.g. `days(ts)`) and Iceberg tracks it
  in metadata — **queries don't need a `WHERE partition_col=` hint**, and you can change the
  partition scheme without rewriting old data (**partition evolution**). (JD: "partitioning".)
- **Time travel & rollback:** query `AS OF` a snapshot/timestamp; roll back a bad write.
- **Compaction:** rewrites many small files into fewer big ones + expires old snapshots →
  faster scans. Run via `rewrite_data_files` / Glue. (JD: "compaction, metadata management".)
- **Hidden partitioning + stats/pruning** = "efficient storage and query performance" bullet.

**Q: Iceberg vs Delta Lake vs Hudi?** (JD lists all three)
- **Iceberg:** engine-agnostic (Spark, Flink, Trino, Athena, Snowflake), best partition &
  schema evolution, hidden partitioning. Vendor-neutral (Apache).
- **Delta Lake:** born from Spark/Databricks, transaction log (`_delta_log`), great in the
  Databricks ecosystem, strong on merge/upsert.
- **Hudi:** built for **upsert-heavy / streaming / incremental** ingestion (CDC), has
  Copy-on-Write vs Merge-on-Read table types.
- Safe take: "Iceberg for open, multi-engine analytics with heavy schema/partition change;
  Hudi when the workload is record-level upserts / CDC; Delta if you're Databricks-centric."

**Q: What's the small-files problem and how does Iceberg help?** Streaming/frequent writes
create many tiny files → slow scans + metadata bloat. Fix: scheduled **compaction**
(`rewrite_data_files`), **expire_snapshots**, and rewrite manifests.

**Q: Copy-on-Write vs Merge-on-Read?** CoW rewrites data files on update (fast reads, slow
writes); MoR writes delete/update files merged at read time (fast writes, slower reads — good
for streaming). Iceberg supports both via row-level deletes.

---

## 2. AWS Data Stack: S3 + Glue + Athena + Lake Formation + IAM

- **S3:** the storage layer (data lake). Data files (Parquet) + Iceberg metadata live here.
- **Glue Data Catalog:** the **metastore** — table/schema definitions Athena/Spark read.
  Glue **Crawlers** infer schema; Glue **ETL Jobs** run **PySpark** (this connects to the
  PySpark bullet — Glue jobs ARE PySpark most of the time).
- **Athena:** serverless **SQL query engine** (Trino/Presto-based) over S3 via the Glue
  Catalog. Supports Iceberg tables natively. Pay-per-TB-scanned → **partitioning + columnar
  Parquet + compression cut cost**. This is likely your **dbt-athena** target.
- **Lake Formation:** central **fine-grained access control** for the lake — table/column/row
  level permissions, layered on top of IAM. (JD: "IAM and security controls" + healthcare = PHI
  → this matters a LOT. Tie to HIPAA.)
- **IAM:** identity & access (roles, policies, least privilege). Glue jobs assume IAM roles to
  read S3/write catalog.

**Q: How would you secure PHI in this lake?** Lake Formation column/row-level permissions +
IAM least-privilege roles + S3 encryption (SSE-KMS) + encryption in transit + CloudTrail audit
logging + tag-based access. (Ties directly to the ISMS/HIPAA section — huge for healthcare.)

**Q: Athena cost/performance levers?** Partition pruning, columnar Parquet, compression
(Snappy/ZSTD), compaction of small files, `LIMIT` won't reduce scan — filter on partitions,
use `EXPLAIN`, avoid `SELECT *`.

---

## 3. dbt (you have real experience — lean in)

- **What/why:** transformation-as-code in SQL; brings software engineering to analytics —
  version control, modularity (`ref()`), testing, docs, lineage.
- **`ref()` / `source()`:** build a DAG of models; dbt handles run order + dependency graph.
- **Materializations:** `view` (what you used), `table`, **`incremental`** (only process new
  rows — critical at scale, know the `is_incremental()` + unique_key pattern), `ephemeral`.
- **Tests:** generic (`unique`, `not_null`, `accepted_values`, `relationships`) + singular
  (custom SQL) + `dbt_utils`. **This is the JD's "data quality frameworks / validation layers".**
- **Sources + freshness:** declare raw sources, add `freshness` checks (SLA monitoring →
  "observability").
- **dbt on AWS:** **dbt-athena** or **dbt-glue** adapter writes **Iceberg** tables. Mention this
  to bridge your Snowflake work to their stack.

**Q: How do you make an incremental model?** Materialize `incremental`, set `unique_key`, and
guard the "only new rows" filter with `{% if is_incremental() %} WHERE updated_at > (select
max(updated_at) from {{ this }}) {% endif %}`. On Iceberg use `incremental_strategy='merge'`.

**Q: How do you test data quality in dbt?** `schema.yml` tests + freshness + custom singular
tests + store failures for triage; wire `dbt test` as an Airflow task that fails the pipeline
(exactly your delayed-orders instinct, but native).

---

## 4. Orchestration: Airflow (you know it) + Step Functions

- **Airflow:** DAGs, operators, tasks, dependencies (`>>`), scheduling, retries,
  `email_on_failure` (you used all of these). Know: **XComs** (pass data between tasks),
  **Sensors** (wait for a condition/file), **idempotency & backfills** (`catchup`), **Connections
  & Variables** (secrets — the fix for your hardcoded paths/creds).
- **Step Functions:** AWS-native **serverless orchestration** (state machine of Lambda/Glue/
  Athena steps). Compare: Airflow = rich, code-first, great for complex DAGs & backfills, you
  run/manage it; Step Functions = serverless, pay-per-transition, tight AWS IAM integration,
  simpler for AWS-only linear/branching flows. "Airflow for complex data-DAGs; Step Functions
  when it's a lightweight AWS-native workflow gluing Glue/Lambda/Athena."

**Q: Task failed at 2am — how do you debug?** Check task logs in the UI, identify retry
behavior, check upstream data freshness, is it idempotent to re-run?, alerting caught it (like
my email_on_failure), root-cause vs re-run. Mention **idempotency** so a re-run is safe.

---

## 5. PySpark / Spark

- **Why Spark:** distributed processing of data too big for one machine; the engine behind
  Glue ETL and big Iceberg writes.
- **Core concepts:** DataFrame API, **lazy evaluation** (transformations vs actions),
  **partitions**, **shuffle** (expensive — joins/groupBy), **wide vs narrow transformations**,
  `cache()/persist()`, **broadcast join** for small-large joins, handling **data skew** (salting).
- **Common ops:** `read.parquet`, `filter/select/withColumn/groupBy/join`, `write.format("iceberg")`.
- **Perf levers:** partition pruning, predicate/column pushdown, avoid `collect()` on big data,
  right partition count, broadcast small dims, minimize shuffles.

**Q: Narrow vs wide transformation?** Narrow (map/filter) = no shuffle, data stays on partition;
wide (groupBy/join) = shuffle across the network → the expensive part. Optimize by reducing
shuffles and broadcasting small tables.

**Q: How to handle skew?** Salting keys, broadcast join, AQE (Adaptive Query Execution) in
Spark 3+ auto-handles some skew.

---

## 6. Data Quality, Observability, Reliability (JD emphasizes this)

- **Validation layers:** dbt tests, Great Expectations / AWS Glue Data Quality (DQDL),
  schema enforcement, null/range/uniqueness/referential checks.
- **Observability:** freshness SLAs, row-count anomaly detection, pipeline metrics, lineage,
  alerting (your email-on-failure is the seed of this). Tools: dbt freshness, CloudWatch,
  data-observability platforms (Monte Carlo-style concepts).
- **Reliability:** idempotency, retries with backoff, dead-letter handling, backfills,
  circuit-breaker gates that stop bad data propagating (your DELAYED gate = a quality gate).
