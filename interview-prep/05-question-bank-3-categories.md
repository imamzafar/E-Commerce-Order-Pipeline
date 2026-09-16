# MASTER QUESTION BANK — 3 Categories (+ Behavioral)
Interview: Fri Sep 18, 2026, 12:00pm IST · 30 min · Soumyajit Datta (DE Manager)

> HOW TO USE: For each question, cover the bolded key points in your OWN words out loud.
> No AI/notes allowed in the actual call — rehearse until these are reflexes.
> 30 min is SHORT: expect ~intro + 6–10 real questions. Depth per answer: 60–120 sec.

═══════════════════════════════════════════════════════════════════════════════
# STRATEGY IN ONE LINE
Thread all three worlds: **"Medallion lakehouse on Delta + PySpark (my daily) · real
Snowflake migration (his world) · shipped on AWS Glue/S3 + dbt + Airflow (the JD)."**
Your observability win (20%→1–2% failures) is your headline story — use it everywhere.
═══════════════════════════════════════════════════════════════════════════════


███████████████████████████████████████████████████████████████████████████████
# CATEGORY 1 — FROM YOUR RESUME (highest probability he asks these)
███████████████████████████████████████████████████████████████████████████████

## Q1. "Tell me about yourself." (100% certain)
- 4+ yrs, Senior DE, Databricks-certified (Professional + Associate).
- Daily: Azure Databricks medallion pipelines, PySpark, Delta, Unity Catalog, Event Hub streaming.
- Headline win: built observability + lineage framework → cut daily pipeline failures ~20%→1–2%.
- Range: full SAS→**Snowflake** migration (hotel group); AWS Glue/S3 + dbt + Airflow (US QSR).
- Close forward: "excited by this role because it's the lakehouse + AWS + healthcare work I want
  to go deeper on." Keep to ~75 sec. DON'T recite the whole resume.

## Q2. "Walk me through your current project / most complex pipeline." (very likely)
- Context: FTSE 100 consumer-health group, ~200 markets. Medallion (bronze/silver/gold) on Databricks.
- The hard problem: ~20% of daily pipelines failed, cascading into dependent jobs; triage was manual.
- What you did: (1) root-caused recurring failures, isolated failure-prone jobs so one failure
  doesn't cascade; (2) built an **observability framework** — end-to-end pipeline health incl.
  edge-case failures; (3) built **lineage** linking Power BI reports → upstream failures so business
  impact is traceable; (4) integrated 5 sources (Power BI REST API, AAS cube API, Databricks API,
  ADF via Event Hub, SharePoint) into one telemetry view; (5) batch + streaming ingest via Event Hub.
- Result: failures 20%→1–2%; triage + stakeholder comms time cut sharply.
- Have READY: "the single hardest bug" and "a design tradeoff I made" — he'll drill one level down.

## Q3. "What is medallion architecture? Why bronze/silver/gold?" (likely — core to your resume)
- **Bronze** = raw, as-ingested (immutable landing, schema-on-read, full history/replayability).
- **Silver** = cleaned, conformed, deduped, validated, joined — the trusted layer.
- **Gold** = business-level aggregates / analytics-ready marts for BI & consumers.
- Why: separation of concerns, reprocessability from bronze, quality gates between layers,
  reusable curated data. BRIDGE: "same idea as dbt staging→intermediate→marts, and it maps
  cleanly onto an Iceberg-on-S3 lakehouse."

## Q4. "You migrated SAS to Snowflake — walk me through it." (HIS FAVORITE — Snowflake!)
- Hotel group, 30+ brands, 130+ countries. Legacy SAS → Snowflake, owned several modules E2E.
- Translated SAS logic → Snowflake SQL + **stored procedures**; validated parity vs legacy outputs.
- **Optimised** legacy code + Snowflake queries → better runtime + lower warehouse compute cost.
- Built Python automation for account tracking/reconciliation (replaced manual work).
- Be ready for: "how did you validate migration correctness?" (row/aggregate reconciliation,
  parity testing old vs new), "how did you cut Snowflake cost?" (right-size warehouse,
  auto-suspend, pruning, avoid SELECT *, clustering big tables, cut full-refreshes).

## Q5. "How did you cut pipeline failures from 20% to 1–2%?" (your headline — nail the HOW)
- Diagnosed recurring **root causes** (not symptoms); categorized failure classes.
- **Isolated** failure-prone jobs → decoupled dependencies so one failure ≠ cascade.
- Built observability to catch edge cases that previously went undetected; lineage for fast triage.
- Added proactive alerting + RCA automation. Frame it as reliability engineering, not luck.

## Q6. "Your resume mentions AI-assisted engineering / Claude Code. Tell me about that."
  (LIKELY + DELICATE — remember they BAN AI in interviews)
- Frame: "AI is a **productivity multiplier on the mechanical parts** — boilerplate, refactors,
  test scaffolding — I still **own architecture, correctness, performance and security**, and I
  **review every generated change**." ~50% faster with review in the loop.
- CRUCIAL: show YOU drive the thinking. Never imply AI does your design or that you can't without it.
- If he seems skeptical: "The judgment is mine — AI just types faster than me. Happy to whiteboard
  any of this from scratch." (Then you must actually be able to — hence fundamentals below.)

## Q7. "You have 4+ years; this role asks for 5+. Talk to me about that." (possible — stay calm)
- Don't apologize. "In 4 years I've owned end-to-end architecture, led migrations, mentored juniors,
  and run client conversations directly — the scope and seniority of work matches a 5+ profile.
  I'm Databricks-Professional certified and I've delivered for FTSE 100 / Fortune 500 clients."
  Redirect to impact, not tenure.

## Q8. Likely resume follow-ups (be ready, 1–2 lines each):
- "What's Unity Catalog and why did you use it?" → central governance: access control, lineage,
  auditability across workspaces; 3-level namespace (catalog.schema.table). BRIDGE → Lake Formation.
- "Streaming with Event Hub — batch vs streaming, how?" → Event Hub (Kafka-like) → Structured
  Streaming / Auto Loader into bronze; micro-batch; checkpointing for exactly-once-ish.
- "dbt tests you used?" → not_null, unique, accepted_values, relationships + freshness; ran via
  Airflow so bad data fails the pipeline before reporting.
- "CI/CD for pipelines?" → Git-based, environment promotion, automated deploy, fewer manual errors.
- "Biggest production incident you handled?" → have one STAR story ready.


███████████████████████████████████████████████████████████████████████████████
# CATEGORY 2 — FROM THE JD (their stack; where your gaps are — study hard)
███████████████████████████████████████████████████████████████████████████████

## Q9. "How comfortable are you with Apache Iceberg?" (JD names it twice, 'preferred')
- Honest bridge: "I work with **Delta Lake** daily — same table-format concept: ACID over Parquet
  on object storage, snapshots, time travel, schema evolution. Iceberg's the open, engine-agnostic
  cousin. I've studied its model — hidden partitioning, partition evolution, manifest metadata,
  compaction — and I'm confident ramping fast because the mental model transfers 1:1."
- Then show you know specifics (see 01-tech-deep-dives): metadata layers, schema evolution by
  column ID, hidden partitioning, snapshots/rollback, compaction/`rewrite_data_files`, small-files.

## Q10. "Delta vs Iceberg vs Hudi — differences?"
- Delta: Spark/Databricks-native, `_delta_log`, great merge/upsert. (You know this.)
- Iceberg: open, multi-engine (Athena/Trino/Spark/Snowflake), best schema+partition evolution,
  hidden partitioning.
- Hudi: upsert/CDC/streaming-first, Copy-on-Write vs Merge-on-Read.
- Take: "Delta if Databricks-centric; Iceberg for open multi-engine analytics; Hudi for
  record-level CDC ingestion."

## Q11. "Walk me through how you'd build a pipeline on their stack (S3 + Glue + Athena + Iceberg)."
- Ingest → land raw in **S3** (bronze). Transform with **Glue (PySpark)** or **dbt-athena** writing
  **Iceberg** tables (silver/gold). Catalog in **Glue Data Catalog**. Query via **Athena**.
  Govern with **Lake Formation** (column/row access) + IAM least-privilege. Orchestrate with
  **Airflow or Step Functions**. Data quality via dbt tests / Glue Data Quality. Observability +
  alerting. "It's my medallion pattern, AWS-native."

## Q12. "What do you know about Glue / Athena / Lake Formation?"
- Glue: serverless Spark ETL + Data Catalog (metastore) + crawlers. (You've written Glue scripts.)
- Athena: serverless SQL (Trino) over S3 via Glue Catalog; bills per TB scanned → partition +
  Parquet + compression to cut cost; supports Iceberg.
- Lake Formation: fine-grained (table/column/row) access control on the lake, on top of IAM.
  BRIDGE: "the AWS analog of Unity Catalog, which I run today."

## Q13. "Airflow vs Step Functions?" (JD lists both)
- Airflow: code-first, rich DAGs, backfills, big ecosystem — you run/manage it. (You know it.)
- Step Functions: serverless AWS-native state machine, pay-per-transition, tight IAM/Glue/Lambda
  integration, simpler AWS-only flows.
- Take: "Airflow for complex data DAGs & backfills; Step Functions for lightweight AWS-native
  orchestration gluing Glue/Lambda/Athena."

## Q14. "Near-real-time pipelines — how?" (JD: 'batch and near-real-time')
- Streaming ingest (Event Hub/Kafka/Kinesis) → Structured Streaming / Auto Loader / Snowpipe →
  micro-batch into bronze → incremental transforms. You've done Event Hub streaming — say so.

## Q15. "Data quality & observability at scale — your approach?" (JD emphasizes; YOUR strength)
- Validation: dbt tests + schema enforcement + null/range/uniqueness/referential + Great
  Expectations / Glue Data Quality.
- Observability: freshness SLAs, row-count anomaly detection, lineage, alerting — exactly the
  framework you built (20%→1–2%). This is your strongest JD match — lean in hard.

## Q16. "Healthcare data — PHI/HIPAA/security awareness?" (JD has whole ISMS section)
- "Security as a design constraint: PHI encrypted at rest (KMS/S3) + in transit (TLS),
  least-privilege IAM, **Lake Formation** column/row access so analysts see only what they're
  authorized to, audit logging (CloudTrail), no PHI in logs or non-prod." Mention you already
  run governance via Unity Catalog. ISMS: you follow security policies, flag/treat risks, support
  BCP. Most candidates skip this — it's an easy standout.


███████████████████████████████████████████████████████████████████████████████
# CATEGORY 3 — FROM INTERVIEWER'S LINKEDIN (his world → rapport + likely probes)
███████████████████████████████████████████████████████████████████████████████
Soumyajit: 12+ yrs DWH. Snowflake(+Snowpipe), Teradata, Informatica PC + IICS/IDMC, OpenFlow
(Apache NiFi), Python + Unix scripting, Oracle/MongoDB/SQL Server/DB2. Domains: insurance, retail,
sports, aviation. He is an INGESTION + ETL + WAREHOUSING person.

## Q17. "Explain Snowflake architecture." (very likely — his core)
- 3 decoupled layers: **storage** (micro-partitions, columnar, on object store), **compute**
  (virtual warehouses — independent MPP clusters, scale up/out), **cloud services** (optimizer,
  metadata, security, result cache). Storage/compute separation = independent scaling + shared data.

## Q18. "How does Snowpipe work? How would you do continuous ingestion?" (HIS DAILY WORK)
- Files land in S3 external stage → event notification (SNS/SQS) → Snowpipe auto `COPY INTO`,
  serverless, near-real-time. vs bulk COPY (scheduled, uses a warehouse). Streams+Tasks for CDC.
- You've used `snowflake-connector-python` (your e-commerce project!) — say you've written Python
  that ingests into Snowflake.

## Q19. "ETL vs ELT?" (he's a lifelong Informatica ETL guy — be respectful)
- ETL (Informatica): transform before load — good when target compute is expensive/rigid.
- ELT (modern cloud): load raw, transform in-warehouse/lakehouse with SQL/dbt — leverages elastic
  compute, keeps raw for replay. "Both valid; I lean ELT on cloud lakehouses but respect ETL's
  strengths for controlled, governed enterprise flows." DON'T dismiss Informatica.

## Q20. "Have you worked with Teradata / Informatica / NiFi?" (he may check overlap)
- Be honest: "Not hands-on Teradata/Informatica — my warehousing is Snowflake + Databricks SQL,
  and my ETL/ELT is PySpark + dbt + Airflow. I understand the concepts they implement and I ramp
  fast on tools." Recognize **OpenFlow = Apache NiFi** (flow-based ingestion) — naming it earns points.

## Q21. Warehousing fundamentals (Teradata/Snowflake veteran WILL touch at least one):
- **SCD Type 1 vs Type 2** (Type 2 keeps history: effective dates + current flag + surrogate keys).
  You have this on your resume — be crisp.
- **Star vs Snowflake schema**; fact vs dimension; grain of a fact table; surrogate keys.
- Normalization vs denormalization for analytics; why star schemas for BI.

## Q22. "Python + Unix scripting for ingestion?" (his stated focus)
- Python: API/DB extraction, pandas, connectors, orchestration glue, reconciliation (you did
  reconciliation scripts at Tredence). Unix: cron, file watching, sed/awk/grep, staging files.
  Say you're comfortable scripting ingestion pipelines end to end.


███████████████████████████████████████████████████████████████████████████████
# CATEGORY 4 — BEHAVIORAL / FIT + LIVE SQL (always in a 30-min HM screen)
███████████████████████████████████████████████████████████████████████████████

## Behavioral (prep 1 STAR story each — Situation/Task/Action/Result, quantify):
- "Time you improved performance/cost." → Snowflake tuning / Delta optimization / cutting failures.
- "A data quality incident." → your observability framework story.
- "Disagreement / tough design tradeoff." → show you weigh options and commit.
- "Mentored a junior." → you do this (resume) — have a concrete example.
- "Drove something design→production." → medallion platform or SAS→Snowflake migration.
- "Why Cohere Health? / Why leave current role?" → growth into AWS+healthcare platform work;
  stay positive about current employer. Do a 5-min read on Cohere (prior-auth / clinical intelligence).

## LIVE SQL (very likely — he's SQL-deep). Practice OUT LOUD before the call:
- **2nd highest salary** (or Nth) → `DENSE_RANK() OVER (ORDER BY salary DESC)`.
- **Top N per group** → `ROW_NUMBER() OVER (PARTITION BY dept ORDER BY sales DESC)`.
- **Deduplication** → ROW_NUMBER partition by key, keep rn=1.
- **Running total / cumulative** → `SUM(x) OVER (PARTITION BY .. ORDER BY .. ROWS UNBOUNDED PRECEDING)`.
- **Find gaps / consecutive** → LAG/LEAD.
- **JOIN types** + when each; **GROUP BY + HAVING**; **CTEs** for readability.
- Know difference: WHERE vs HAVING, RANK vs DENSE_RANK vs ROW_NUMBER, UNION vs UNION ALL.

## YOUR questions to ask him (pick 3–4 — shows seniority):
- "How far along is the Iceberg migration — greenfield or modernizing Snowflake/legacy?"
- "What's the current orchestration — Airflow, Step Functions, or both?"
- "How do you handle PHI access control across the lake today?"
- "As the DE Manager, what does success look like for this role at 3 and 6 months?"
- "What are the biggest data reliability challenges the team is tackling now?"


═══════════════════════════════════════════════════════════════════════════════
# TOP-10 MOST LIKELY (if you only prep 10, prep these)
1. Tell me about yourself.               6. Iceberg / Delta-vs-Iceberg (bridge).
2. Walk me through your current project.  7. ETL vs ELT.
3. SAS→Snowflake migration story.         8. Data quality/observability approach.
4. Snowflake architecture.                9. A live SQL question (window function).
5. Snowpipe / continuous ingestion.      10. Why Cohere Health? + your questions.
═══════════════════════════════════════════════════════════════════════════════
