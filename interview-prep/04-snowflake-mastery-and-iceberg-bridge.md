# Snowflake Mastery + Snowflake→Iceberg Bridge (THE key page for Soumyajit)

Your interviewer is a Snowflake/Teradata/Informatica veteran. Be genuinely strong on Snowflake,
then bridge every concept to the JD's Iceberg/AWS stack. That combo = rapport + range.

═══════════════════════════════════════════════════════════════════════
## PART A — SNOWFLAKE (be able to explain each cold, in plain words)
═══════════════════════════════════════════════════════════════════════

### Architecture (his favorite topic — nail this)
- **3 decoupled layers:**
  1. **Storage** — data stored compressed, columnar, in **micro-partitions** on cloud object
     storage (S3/Azure/GCS). You don't manage it.
  2. **Compute** — **Virtual Warehouses** (independent MPP clusters). Multiple warehouses hit
     the same data with no contention. Scale up (bigger) or out (multi-cluster for concurrency).
  3. **Cloud Services** — the brain: query optimization, metadata, security, transactions,
     result cache.
- **Why it matters:** separation of storage & compute = you pay for each independently, scale
  compute instantly, and many teams share one copy of data. **(This is the SAME principle as
  S3 + Athena/Spark/EMR — storage on S3, compute is separate & elastic.)**

### Micro-partitions & clustering
- Snowflake auto-splits tables into **micro-partitions** (~50–500MB uncompressed, columnar) and
  stores **min/max/count metadata** per partition → **partition pruning** skips irrelevant ones.
- **Clustering keys:** for very large tables, define a clustering key so related rows co-locate →
  better pruning. Auto-clustering maintains it.
- **BRIDGE → Iceberg:** micro-partition metadata ≈ Iceberg's **manifest files with column
  stats**; pruning is the same idea. Iceberg adds **hidden partitioning** (you don't hint the
  partition column) and **partition evolution** (change scheme without rewriting old data) —
  Snowflake handles partitioning fully automatically, so it's a natural concept for you.

### Data loading / ingestion
- **COPY INTO** — bulk load from a **stage** (internal or external S3 stage) into a table.
- **Snowpipe** — **continuous / near-real-time** micro-batch ingestion; auto-triggered by cloud
  event notifications (e.g., S3 → SNS/SQS) as files land. Serverless.
- **Streams + Tasks** — **Stream** = CDC (tracks row changes on a table); **Task** = scheduled
  SQL/procedure. Stream+Task = build incremental ELT pipelines inside Snowflake.
- **BRIDGE → AWS:** Snowpipe (event-driven S3 ingest) ≈ **S3 event → Lambda/Glue** or
  **Kinesis→S3**; Streams (CDC) ≈ **Hudi/Iceberg upserts** or **DMS CDC**; Tasks ≈ **Airflow/
  Step Functions** schedules. "near-real-time pipelines" in the JD = the Snowpipe pattern.

### Snowpipe + Python ingestion + OpenFlow/NiFi + Unix (HIS DAILY WORK — prioritize)
- **Snowpipe (know this deeply):** serverless, continuous micro-batch loading. Files land in an
  S3 (external) stage → S3 event notification (SNS/SQS) → Snowpipe auto-runs `COPY INTO`. Use
  it for near-real-time file ingestion without managing a warehouse. Alternative trigger: the
  Snowpipe REST API. Contrast with bulk `COPY INTO` (manual/scheduled, uses a warehouse).
- **Python ingestion:** `snowflake-connector-python` (you've USED this in your project's
  check_delayed_orders.py!) + `write_pandas` / SQLAlchemy / Snowpark to load & transform.
  Common pattern: Python pulls from an API/DB → lands files in S3 stage → Snowpipe loads →
  dbt transforms. You can honestly say you've written Python that connects to Snowflake.
- **OpenFlow (Apache NiFi):** Snowflake's OpenFlow is built on **Apache NiFi** — a visual,
  flow-based data ingestion/routing tool (processors, flowfiles, back-pressure). It's for
  moving data from many sources into Snowflake. Just know *what it is* and that it's an
  ingestion/integration layer — he'll be impressed you even recognize it.
- **Unix/shell scripting:** cron jobs, file watching, `sed/awk/grep`, moving files to stages,
  wrapping loads. Be ready to say you're comfortable scripting ingestion glue in bash.

### Time travel & cloning
- **Time Travel:** query/restore data **AS OF** a past timestamp or before a DML (default 1 day,
  up to 90 on Enterprise). `SELECT ... AT(OFFSET => -3600)`; `UNDROP TABLE`.
- **Zero-copy cloning:** `CREATE TABLE x CLONE y` — instant, no storage duplication (metadata
  pointers), great for dev/test copies of prod.
- **Fail-safe:** 7-day Snowflake-managed recovery after time-travel window.
- **BRIDGE → Iceberg:** Time Travel ≈ Iceberg **snapshots / time travel / rollback** — SAME
  concept (query a past snapshot, roll back a bad write). Say this out loud in the interview.

### Performance & cost (managers LOVE cost awareness)
- **Result cache** (24h, free re-run of identical query), **warehouse cache** (data cached on
  warehouse SSD).
- **Levers:** right-size warehouse, auto-suspend/auto-resume (don't pay idle), clustering on big
  tables, avoid `SELECT *`, prune with filters, materialized views for hot aggregates,
  multi-cluster warehouses for concurrency spikes.
- **Cost model:** compute billed per-second per warehouse (credits) + storage. Auto-suspend =
  #1 cost saver.
- **BRIDGE → Athena:** Athena bills **per TB scanned** → partitioning + columnar Parquet +
  compression + compaction are the cost levers (vs Snowflake's per-second compute). Know the
  difference — it shows platform range.

### Modeling / warehousing fundamentals (Teradata guy WILL touch these)
- **Star vs snowflake schema**, fact vs dimension tables, **SCD Type 1/2** (slowly changing
  dimensions — Type 2 keeps history with effective dates / current flag), grain of a fact table,
  surrogate keys, normalization vs denormalization for analytics.
- **ELT vs ETL:** modern cloud = **ELT** (load raw, transform in-warehouse with dbt) vs classic
  Informatica **ETL** (transform before load). Be ready to contrast — he did years of Informatica
  ETL; frame ELT/dbt as the modern evolution, respectfully.
- Snowflake specifics: **VARIANT** type for semi-structured JSON, `LATERAL FLATTEN`, external
  tables over S3, secure views, RBAC roles.

### Snowflake governance/security (ties to healthcare/PHI)
- RBAC roles, column-level security / **masking policies**, **row access policies**, network
  policies, data encryption (always-on). Maps to Lake Formation's column/row-level control on AWS.

═══════════════════════════════════════════════════════════════════════
## PART B — ONE-GLANCE BRIDGE TABLE (memorize this)
═══════════════════════════════════════════════════════════════════════

| Concept                | Snowflake (you know)          | JD / AWS-Iceberg (their stack)          |
|------------------------|-------------------------------|-----------------------------------------|
| Storage/compute split  | Storage layer + Virtual WHs   | S3 + Athena/EMR/Glue (separate compute) |
| Storage format         | Micro-partitions (managed)    | Parquet files + Iceberg metadata on S3  |
| Partition pruning      | Micro-partition min/max meta  | Iceberg manifest column stats           |
| Partitioning           | Automatic / clustering keys   | Hidden partitioning + partition evolution|
| Time travel / rollback | Time Travel + UNDROP          | Iceberg snapshots + rollback            |
| Schema change          | ALTER, flexible               | Iceberg schema evolution (by column ID) |
| Continuous ingest      | Snowpipe (S3 event → load)    | S3 event → Lambda/Glue, Kinesis         |
| CDC / incremental      | Streams + Tasks               | Hudi/Iceberg merge, DMS CDC             |
| Transform layer        | dbt-snowflake                 | dbt-athena / dbt-glue (SAME dbt!)       |
| Orchestration          | Tasks / Airflow               | Airflow / Step Functions                |
| Governance             | RBAC, masking, row policies   | Lake Formation + IAM                    |
| Cost lever             | Auto-suspend, right-size WH   | Partition/compress → less TB scanned    |

**The killer line:** "dbt is the constant across both worlds — my dbt modeling skills transfer
1:1; only the adapter and storage engine change underneath."

═══════════════════════════════════════════════════════════════════════
## PART C — LIKELY QUESTIONS FROM HIM SPECIFICALLY
═══════════════════════════════════════════════════════════════════════
- "Walk me through Snowflake's architecture." → the 3 layers, storage/compute decoupling.
- "How does Snowflake handle partitioning?" → micro-partitions + pruning + clustering keys.
- "How would you load streaming data?" → Snowpipe + event notifications; Streams+Tasks for CDC.
- "Difference between ETL and ELT?" → and why cloud warehouses favor ELT + dbt.
- "How do you optimize a slow Snowflake query / control cost?" → pruning, warehouse sizing,
  auto-suspend, result cache, clustering, avoid SELECT *.
- "You know Snowflake — how comfortable are you moving to Iceberg on AWS?" → THE bridge answer:
  same concepts, dbt transfers, I've started learning, excited. (Use the bridge table.)
- "Explain SCD Type 2." / "Star vs snowflake schema." → warehousing fundamentals.
- A **live SQL** question (very likely): window functions (ROW_NUMBER/RANK for dedup &
  top-N-per-group), joins, aggregation, date diffs. PRACTICE these out loud.
