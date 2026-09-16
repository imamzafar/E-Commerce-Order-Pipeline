# HANDOFF BRIEF — Interview Prep for Zafar Imam (for another AI agent)

> **You are being handed a task.** Zafar Imam is preparing for a job interview and wants you
> to help him get ready. This document is fully self-contained — everything you need is below.
> Read it top to bottom, then help him per the "YOUR JOB" and "HOW TO HELP" sections.
> Prepared: 2026-09-16. Interview date: **2026-09-18, 12:00pm IST.**

═══════════════════════════════════════════════════════════════════════════════
# 0. TL;DR FOR THE AGENT
═══════════════════════════════════════════════════════════════════════════════
- Candidate: **Zafar Imam**, Senior Data Engineer, 4+ yrs, Databricks-certified (Pro+Assoc).
- Job: **Senior Data Engineer @ Cohere Health** (healthcare, AWS + Apache Iceberg lakehouse).
- Interviewer: **Soumyajit Datta**, Data Engineering Manager — a 12+ yr **Snowflake / Teradata /
  Informatica** warehousing & ingestion veteran.
- The tension: candidate's daily stack is **Azure Databricks / Delta / PySpark**; the JD is
  **AWS / Iceberg**; the interviewer lives in **Snowflake**. Three different centers of gravity.
- Strategy: **thread all three** — "Medallion lakehouse on Delta + PySpark (my daily) · real
  Snowflake migration (his world) · shipped on AWS Glue/S3 + dbt + Airflow (the JD)."
- Interview rule: **NO AI / real-time assistance allowed DURING the call** (disqualification
  risk). So all help is PREP beforehand; on the call he's solo and must own fundamentals himself.
- Format: 30-min first-round hiring-manager screen → expect intro + ~6–10 questions + his Q&A.
- Your main job: **run realistic mock interviews and coach**, plus fill knowledge gaps
  (Iceberg, Athena, Lake Formation, Step Functions) and drill live SQL.

═══════════════════════════════════════════════════════════════════════════════
# 1. THE CANDIDATE (from his resume)
═══════════════════════════════════════════════════════════════════════════════
**Zafar Imam** · Senior Data Engineer · imamzafar100@gmail.com · +91 82288 85190
· linkedin.com/in/zafarimammm · Hyderabad, India · Indian National · Notice: 15 days.

**Summary:** Databricks Certified Data Engineer (Professional + Associate, Aug 2026). 4+ yrs
building enterprise-scale data platforms for Fortune 500 / FTSE 100 clients on Azure Databricks,
PySpark, Snowflake, AWS. Currently architecting medallion (bronze/silver/gold) pipelines with
Unity Catalog governance + Event Hub streaming. Owns architecture end to end, reviews code,
mentors juniors, runs client conversations.

**Core skills:**
- Databricks/Big Data: Azure Databricks, Spark, PySpark, Spark SQL, **Delta Lake**, Medallion,
  Unity Catalog (governance/lineage), Databricks Workflows, Spark perf tuning.
- Azure: Databricks, ADF, Event Hub, ADLS.
- Warehousing: **Snowflake** (platform migration, stored procs, tuning), star/snowflake schema,
  SCD 1/2.
- AWS: **Glue, S3**.
- Orchestration/transform: Databricks Workflows, **Airflow, dbt**, ETL/ELT.
- Languages: **Python, PySpark, SQL** (advanced — window functions, optimisation), Pandas.
- Practices: data governance, DQ & observability, CI/CD (Git), perf/cost optimisation, cloud
  migration, streaming ingestion, stakeholder mgmt, mentoring/code review.
- AI-assisted: Claude Code multi-agent (~50% faster, reviews all output). *(See caution in §4.)*
- Working knowledge: Synapse, Delta Live Tables, Auto Loader.

**Experience:**
1. **Quantzig** — DE, FTSE 100 consumer-health, ~200 markets (Hyderabad, Oct 2025–present).
   Medallion on Databricks; **built observability + lineage framework that cut daily pipeline
   failures ~20%→1–2%** (HEADLINE); integrated 5 sources (Power BI REST API, AAS cube API,
   Databricks API, ADF via Event Hub, SharePoint) into one telemetry view; batch+streaming
   ingest via Event Hub; Unity Catalog governance; owns architecture, mentors, client-facing.
2. **Sigmoid** — DE, NASDAQ US QSR chain, 2000+ locations (Bengaluru, Feb–Sep 2025).
   ETL on **AWS Glue, S3, Airflow**, SQL Server; **dbt tests via Airflow** for DQ; CI/CD.
3. **Tredence** — DE, global hotel group, 30+ brands / 130+ countries (Bengaluru, Jul 2022–Jan
   2025). **Full SAS→Snowflake migration**; stored procs; query & warehouse-cost optimisation;
   Python reconciliation automation; daily client comms; 2× Certificate of Appreciation.

**Education:** B.Tech, BIT Sindri, CGPA 8.55/10.

**Known gaps vs the JD:** Apache Iceberg, Athena, Lake Formation, Step Functions. All bridgeable:
Delta≈Iceberg (table format), Unity Catalog≈Lake Formation (governance), Airflow↔Step Functions.
Also **4+ yrs vs the JD's "5+"** — coach him to redirect to scope/impact, not tenure.

═══════════════════════════════════════════════════════════════════════════════
# 2. THE JOB (JD)
═══════════════════════════════════════════════════════════════════════════════
**Senior Data Engineer — Cohere Health, Inc.** (healthcare; prior-authorization / clinical
intelligence; Inc. 5000 fastest-growing 2025). Location: Hyderabad (commute/relocate preferred).
Recruiter: Shyam Adiraju (shyam.adiraju@coherehealth.com).

**Overview:** design & deliver a cloud-native healthcare data platform on AWS, Apache Iceberg,
Lake Formation, Glue Catalog, Athena, dbt, modern orchestration. Hands-on + cross-team collab.

**What you'll do:** deliver complex DE projects; design→production; scalable patterns & reusable
frameworks; **batch and near-real-time pipelines**; reusable ingestion/transformation/validation/
publishing frameworks; modernize legacy workloads; **Apache Iceberg** implementation & optimization
(schema evolution, partitioning, compaction, metadata mgmt); efficient storage/query performance;
**data quality frameworks & validation layers**; observability/monitoring; code reviews; **mentor
juniors**. Plus an **ISMS/security** section (healthcare = PHI, risk assessments, BCP, CISO).

**What you'll need:** 5+ yrs DE; enterprise-scale; **AWS S3, Glue, Athena, Lake Formation**; IAM
& security; **Apache Iceberg** (preferred); **Delta Lake / Hudi**; **dbt**; **Airflow or Step
Functions**; **Python**; **SQL**; **PySpark / Spark**.

**Match map (candidate already has):** PySpark ✅, Delta Lake ✅ (JD lists it!), Glue/S3 ✅, dbt ✅,
Airflow ✅, data quality/observability ✅ (his headline), Snowflake ✅. **Gaps:** Iceberg, Athena,
Lake Formation, Step Functions.

═══════════════════════════════════════════════════════════════════════════════
# 3. THE INTERVIEWER (LinkedIn) — Soumyajit Datta
═══════════════════════════════════════════════════════════════════════════════
- **Data Engineering Manager, Cohere Health** (joined Jun 2026). Hyderabad. 500+ connections.
- **12+ years in DWH / Data Engineering** — his whole career. Domains: **insurance, retail,
  sports, aviation** (not healthcare-native; new to healthcare himself).
- **About (his words):** worked across Snowflake, Snowpipe, **OpenFlow (Apache NiFi)**, Python,
  Oracle, Teradata, MongoDB, SQL, SQL Server, DB2 — "Snowflake being the new one." ETL expertise:
  **Informatica PC, IICS (IDMC)**. Python + **Unix scripting** used rigorously. "Currently
  focusing on Snowflake (Snowpipe) as my warehouse and Python as my ingestion."
- **Top skills:** Informatica PowerCenter, Informatica Cloud, Teradata, Python, Snowflake Cloud.
- **Career:** Cohere (Jun 2026–) ← Entain (Data Eng Specialist) ← Ivy (Sr System Analyst /
  System Analyst) ← Cognizant (Farmers Insurance) ← Capgemini.
- **READ ON HIM:** a classic **ingestion + ETL + enterprise-warehousing** veteran. He speaks
  Snowflake/SQL/warehousing fluently and WILL catch bluffing on them. He is likely LESS deep on
  Iceberg/Spark internals than a platform architect. He values clear thinking, solid modeling,
  SQL, ingestion design, and respect for ETL fundamentals (don't dismiss Informatica).

**Implications for prep:**
- Build genuine Snowflake depth + speak Snowpipe / Python ingestion / a bit of NiFi = instant rapport.
- Bridge every Snowflake concept to the JD's Iceberg/AWS ("same idea, different engine").
- Expect at least one **live SQL** question and one **warehousing fundamentals** question (SCD2,
  star schema, ETL vs ELT).

═══════════════════════════════════════════════════════════════════════════════
# 4. STRATEGY & KEY CAUTIONS (candidate's instructions + my suggestions)
═══════════════════════════════════════════════════════════════════════════════
**Winning narrative (one line):** "Medallion lakehouse on Delta + PySpark (my daily) · real
Snowflake migration (his world) · shipped on AWS Glue/S3 + dbt + Airflow (the JD)."

**Use the headline everywhere:** the observability framework that cut failures **20%→1–2%** is
his strongest, most quantified story — deploy it for reliability, data-quality, and impact questions.

**Bridge gaps honestly, never bluff:**
- Iceberg ← "I use Delta daily; same table-format concept (ACID/Parquet/snapshots/time-travel/
  schema evolution). Iceberg is the open, engine-agnostic cousin — I ramp fast."
- Lake Formation ← "AWS analog of Unity Catalog, which I run today."
- Athena ← serverless SQL over S3, bills per TB scanned → partition/Parquet/compression to cut cost.
- Step Functions ← serverless AWS-native orchestration vs Airflow's code-first DAGs.

**⚠️ CAUTION 1 — the AI question (important):** His resume markets "AI-assisted / Claude Code,
50% faster." BUT this interview **bans AI and wants HIS OWN thinking**. Frame AI as a productivity
multiplier on mechanical work while HE owns architecture/correctness/security and reviews every
change. Never imply AI does his design. **Coaching priority: he must be able to whiteboard every
concept himself — drill fundamentals hard.**

**⚠️ CAUTION 2 — tenure:** 4+ yrs vs JD's 5+. Redirect to scope: end-to-end ownership, migrations,
mentoring, FTSE 100/Fortune 500 delivery, Databricks-Professional cert. Don't apologize.

**⚠️ CAUTION 3 — respect his world:** He's a lifelong Informatica/ETL/Teradata guy. Present ELT/dbt
as the modern evolution, not a put-down of ETL. Acknowledge OpenFlow=NiFi to earn points.

**Study split:** ~40% Snowflake/warehousing (his turf) · ~35% JD/AWS/Iceberg gaps · ~25% project
stories + live SQL + healthcare/HIPAA + questions to ask.

**Open TODOs:** (1) reply to Shyam confirming receipt of the invite; (2) run mock interviews;
(3) live SQL practice; (4) 5-min read on Cohere Health.

═══════════════════════════════════════════════════════════════════════════════
# 5. YOUR JOB (agent) + HOW TO HELP
═══════════════════════════════════════════════════════════════════════════════
**Primary:** run realistic **mock interviews** as Soumyajit, one question at a time, then coach
each answer: (a) what landed, (b) what to tighten, (c) the ideal 60–120s version. Keep it
conversational and time-boxed (30-min screen simulation).

**Question priority (the Top-10 most likely):**
1. Tell me about yourself.                 6. Iceberg / Delta-vs-Iceberg (bridge).
2. Walk me through your current project.    7. ETL vs ELT.
3. SAS→Snowflake migration story.           8. Data quality / observability approach.
4. Snowflake architecture.                  9. A live SQL question (window function).
5. Snowpipe / continuous ingestion.        10. Why Cohere Health? + his questions to ask.

**Coaching principles:**
- Push for concrete, quantified STAR answers (Situation/Task/Action/Result).
- Make him articulate the bridge (his skills → their stack) in his own words.
- Insist he can explain fundamentals WITHOUT AI (interview rule).
- Drill live SQL out loud: 2nd-highest salary, top-N-per-group, dedup, running total, LAG/LEAD;
  RANK vs DENSE_RANK vs ROW_NUMBER; WHERE vs HAVING; UNION vs UNION ALL.
- Cover the delicate ones: the AI-assisted question, the 4-vs-5-year question, ETL-vs-ELT tact.
- Fill knowledge gaps on request: Iceberg internals (metadata layers, hidden partitioning,
  partition/schema evolution, compaction, small-files), Glue/Athena/Lake Formation, Step Functions.

**Reference material (all in this `interview-prep/` folder):**
- `MASTER-CONTEXT.md` — single source of truth (candidate/job/interviewer/strategy/status).
- `05-question-bank-3-categories.md` — full Q bank w/ model answers (resume/JD/interviewer/behavioral+SQL).
- `04-snowflake-mastery-and-iceberg-bridge.md` — Snowflake depth + Snowflake→Iceberg bridge table.
- `01-tech-deep-dives-QA.md` — Iceberg, AWS stack, dbt, Airflow, PySpark, DQ.
- `00-your-project-story.md` — project narration. `02-...` — behavioral/HIPAA/questions.
- `03-interviewer-and-logistics.md` — interviewer profile + logistics + no-AI rule.
- `Zafar_Imam_Senior_Data_Engineer_CV.pdf` — the resume.

**Tone:** direct, encouraging, honest. He's strong and well-matched — the job is articulation +
closing a few gaps, not faking skills. Don't over-flatter; give real, specific feedback.
