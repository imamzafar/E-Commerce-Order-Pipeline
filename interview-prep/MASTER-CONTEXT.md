# MASTER CONTEXT — Zafar Imam (read this first, everything in one place)
> Purpose: persistent memory so nothing has to be re-explained. Last updated: 2026-09-16.

═══════════════════════════════════════════════════════════════════════════════
## 1. WHO I AM (candidate)
═══════════════════════════════════════════════════════════════════════════════
- **Name:** Zafar Imam
- **Email:** imamzafar100@gmail.com  ·  **Phone:** +91 82288 85190
- **LinkedIn:** linkedin.com/in/zafarimammm
- **Title:** Senior Data Engineer  ·  Indian National  ·  Based Hyderabad, India
- **Experience:** 4+ years  ·  **Notice period:** 15 days
- **Certifications:** Databricks Certified Data Engineer **Professional** (Aug 2026) +
  **Associate** (Aug 2026); Udemy PySpark crash course.
- **Education:** B.Tech, Birsa Institute of Technology (BIT) Sindri, CGPA 8.55/10
- **Languages:** English (fluent), Hindi (native), Urdu (fluent), Arabic (reading/writing).

### My stack (from resume)
- **Daily / strongest:** Azure Databricks, PySpark, Spark SQL, Delta Lake, Medallion
  (bronze/silver/gold), Unity Catalog (governance/lineage), Databricks Workflows, streaming.
- **Azure:** Databricks, ADF, Event Hub, ADLS.
- **Warehousing:** Snowflake (full platform migration, stored procs, tuning), dimensional
  modelling (star/snowflake), SCD 1/2.
- **AWS:** Glue, S3.
- **Orchestration/transform:** Databricks Workflows, Airflow, dbt, ETL/ELT design.
- **Languages:** Python, PySpark, SQL (advanced — window fns, optimisation), Pandas.
- **Practices:** data governance, DQ & observability, CI/CD (Git), perf/cost optimisation,
  cloud migration, streaming ingestion, stakeholder mgmt, mentoring/code review.
- **AI-assisted:** Claude Code (multi-agent, parallel agents, forked sessions) — ~50% faster,
  reviews every change for correctness/perf/security. (NOTE: downplay in the no-AI interview;
  emphasize I OWN the engineering judgment.)
- **Working knowledge:** Azure Synapse, Delta Live Tables (DLT), Auto Loader.
- **Gaps vs target job:** Apache Iceberg, Athena, Lake Formation, Step Functions (all bridgeable
  from Delta/Unity Catalog/Airflow).

### My work history (resume)
1. **Quantzig** — Data Engineer, FTSE 100 consumer-health (Hyderabad, Oct 2025–present).
   Medallion pipelines on Azure Databricks; **built observability + lineage framework → cut daily
   pipeline failures ~20%→1–2%**; integrated 5 sources (Power BI REST API, AAS cube API,
   Databricks API, ADF via Event Hub, SharePoint); batch+streaming; Unity Catalog; owns
   architecture, mentors juniors, runs client conversations. ← HEADLINE STORY.
2. **Sigmoid** — Data Engineer, NASDAQ US QSR chain (2000+ locations) (Bengaluru, Feb–Sep 2025).
   ETL on AWS Glue, S3, Airflow, SQL Server; **dbt tests via Airflow** for DQ; CI/CD.
3. **Tredence** — Data Engineer, global hospitality group (30+ brands, 130+ countries)
   (Bengaluru, Jul 2022–Jan 2025). **Full SAS→Snowflake migration**; stored procs; query/cost
   optimisation; Python reconciliation automation; client comms; 2× Certificate of Appreciation.

═══════════════════════════════════════════════════════════════════════════════
## 2. THE JOB
═══════════════════════════════════════════════════════════════════════════════
- **Role:** Senior Data Engineer, **Cohere Health, Inc.** (healthcare — prior authorization /
  clinical intelligence). Inc. 5000 fastest-growing 2025.
- **Location:** Hyderabad, Telangana (commute/relocate preferred).
- **Recruiter:** Shyam Adiraju, Senior TA Partner — shyam.adiraju@coherehealth.com.
- **Stack:** AWS (S3, Glue, Athena, Lake Formation, IAM), **Apache Iceberg** (preferred),
  Delta Lake/Hudi, dbt, Airflow or Step Functions, Python, SQL, PySpark/Spark.
- **Needs:** 5+ yrs DE, enterprise-scale, batch + near-real-time pipelines, reusable
  ingestion/transformation/validation frameworks, Iceberg optimization (schema evolution,
  partitioning, compaction, metadata), data quality + observability, mentoring, code review.
- **ISMS/security:** healthcare = PHI/HIPAA; risk assessments, BCP, CISO reporting, security policies.
- Full JD: `JD-cohere-health-senior-data-engineer.md`.

═══════════════════════════════════════════════════════════════════════════════
## 3. THE INTERVIEW
═══════════════════════════════════════════════════════════════════════════════
- **When:** Fri **Sep 18, 2026, 12:00–12:45pm IST** (30 min). Google Meet: meet.google.com/yhb-ghpb-ozs
- **Round:** First round with hiring manager.
- **⚠️ NO AI / real-time assistance allowed during the call** (disqualification risk). Prep only.
- **TODO:** reply to Shyam to CONFIRM RECEIPT of the invite.
- **Interviewer: Soumyajit Datta — Data Engineering Manager, Cohere Health** (joined Jun 2026).
  - 12+ yrs DWH/DE. Domains: insurance, retail, sports, aviation.
  - Skills: **Snowflake (+Snowpipe), Teradata, Informatica PC + IICS/IDMC, OpenFlow (Apache NiFi),
    Python + Unix scripting**, Oracle/MongoDB/SQL Server/DB2.
  - His words: "currently focusing on Snowflake (Snowpipe) as my warehouse and Python as ingestion."
  - Read: an **ingestion + ETL/ELT + warehousing** veteran. Respect Informatica/ETL; speak Snowpipe.

═══════════════════════════════════════════════════════════════════════════════
## 4. STRATEGY (one line)
═══════════════════════════════════════════════════════════════════════════════
Thread all three worlds: **"Medallion lakehouse on Delta + PySpark (my daily) · real Snowflake
migration (his world) · shipped on AWS Glue/S3 + dbt + Airflow (the JD)."**
- Headline everywhere: observability win 20%→1–2%.
- Bridge gaps honestly: Delta≈Iceberg, Unity Catalog≈Lake Formation, Airflow↔Step Functions.
- Own the fundamentals yourself (no-AI interview) — be ready to whiteboard anything.
- Split study: ~40% Snowflake/warehousing (his turf) · ~35% JD/AWS/Iceberg gaps · ~25% my
  project stories + SQL + healthcare/HIPAA + questions to ask.

═══════════════════════════════════════════════════════════════════════════════
## 5. FILE INDEX (interview-prep/)
═══════════════════════════════════════════════════════════════════════════════
- `MASTER-CONTEXT.md` ............ this file (start here)
- `JD-cohere-health-senior-data-engineer.md` . full job description
- `00-your-project-story.md` ..... how to narrate my e-commerce project (STAR)
- `01-tech-deep-dives-QA.md` ..... Iceberg, AWS stack, dbt, Airflow, PySpark, DQ + Q&A
- `02-behavioral-healthcare-and-questions.md` . STAR stories, HIPAA/ISMS, questions to ask
- `03-interviewer-and-logistics.md` . Soumyajit profile + logistics + no-AI rule
- `04-snowflake-mastery-and-iceberg-bridge.md` . Snowflake depth + Snowflake→Iceberg bridge table
- `05-question-bank-3-categories.md` . MASTER Q bank: resume / JD / interviewer / behavioral + SQL

═══════════════════════════════════════════════════════════════════════════════
## 6. STATUS / NEXT
═══════════════════════════════════════════════════════════════════════════════
- [x] Saved & pushed all prep to branch claude/new-session-wlnjq7.
- [ ] Reply to Shyam confirming receipt.
- [ ] Run mock interview (Top-10 questions) — drill out loud.
- [ ] Live SQL practice (window functions).
- [ ] 5-min read on Cohere Health (prior-auth / clinical intelligence).
