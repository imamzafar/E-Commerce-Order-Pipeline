# Behavioral, Healthcare/ISMS, and Questions to Ask

## Behavioral (use STAR — Situation, Task, Action, Result). Prep 1 story each:

1. **"Tell me about yourself."** 60–90s: who you are → 5+ yrs data engineering → 1–2 signature
   achievements → why this role (healthcare data platform on AWS/Iceberg excites you). End
   forward-looking, not a resume readout.
2. **"Most complex pipeline you built."** → your e-commerce pipeline OR a bigger work project.
   Emphasize scale, the hard part, and the outcome.
3. **"A time you improved performance / cost."** → partitioning, incremental models, compaction,
   killing full-refreshes, reducing Spark shuffles. Quantify (%, time, $).
4. **"A data quality incident."** → how you detected it, contained it (a gate like your DELAYED
   check), root-caused, and prevented recurrence (added a test). This maps to their DQ bullets.
5. **"Disagreement with a teammate / design tradeoff."** → show you weigh options and commit.
6. **"Mentored a junior engineer."** (JD explicitly: "mentor junior engineers"). Have a real example.
7. **"Time you drove something from design to production."** (JD: "design through production
   deployment"). Walk the lifecycle.

**Tip:** Quantify everything you can (rows/day, latency, cost saved, %). Numbers = seniority.

---

## Healthcare / ISMS / Security (Cohere Health — this is a differentiator, MOST candidates skip it)

The JD has a whole ISMS (Information Security Management System) section. In healthcare you're
handling **PHI (Protected Health Information)**. Show you get this:

- **HIPAA:** US law protecting PHI. As a data engineer: encrypt PHI at rest (S3 SSE-KMS) and in
  transit (TLS), least-privilege access, audit logging (CloudTrail), no PHI in logs, data
  minimization, and access controls (Lake Formation column/row-level).
- **ISMS / ISO 27001 concepts** (JD lists these): risk assessments, risk owners, risk treatment
  plans, security policies, **BCP (Business Continuity Plan)** & DR, **CISO** reporting. You
  don't need to be a security expert — just show awareness that as an engineer you **follow
  security policies, flag risks, and build controls into pipelines** (encryption, access, audit).
- **One-liner to have ready:** "In a healthcare data platform I treat security as a design
  constraint, not an afterthought — PHI encrypted with KMS, Lake Formation for column/row-level
  access so analysts only see what they're authorized to, CloudTrail for audit, and no sensitive
  fields in logs or non-prod environments."
- **Cohere Health context:** they do **prior authorization / clinical intelligence** for health
  plans and providers — i.e., data platform feeding clinical decisioning. (Worth a quick web read
  before the call.)

---

## Smart Questions to Ask THEM (always have 4–5 ready; asking = seniority)

- "How far along is the Iceberg migration — greenfield, or modernizing existing Glue/Snowflake/
  legacy workloads?" (shows you read the JD's "modernize legacy workloads")
- "What does the current orchestration look like — Airflow, Step Functions, or a mix — and are you
  standardizing?"
- "How do you handle PHI access control across the lake today — Lake Formation, tag-based, both?"
- "What does 'near-real-time' mean for your pipelines — streaming (Kafka/Kinesis) or micro-batch?"
- "How is the data team structured, and how do platform/analytics/business teams collaborate?"
- "What are the biggest data reliability or quality challenges the team is tackling right now?"
- "What does success in this role look like at 3 and 6 months?"

---

## Logistics / mindset for interview day (day after tomorrow, 2026-09-18)
- Location note: role is Hyderabad; confirm interview is remote/onsite and time zone.
- Have your project open/ready to screen-share or describe from memory.
- Round 1 is often a mix: 40% your experience (project story), 40% tech (Iceberg/AWS/dbt/SQL),
  20% behavioral + healthcare fit.
- **If you don't know something:** say how you'd find out / reason about it — never bluff.
- Do a **live SQL warm-up** (window functions, joins, dedup) and a **dbt incremental** rehearsal.

## 2-Day Study Plan
**Day 1 (tomorrow):** Iceberg deep dive (metadata layers, schema/partition evolution,
compaction, vs Delta/Hudi) + AWS stack (Glue/Athena/Lake Formation/S3/IAM) + re-read your
project until you can narrate it in 90s without notes.
**Day 2:** dbt (incremental, tests, dbt-athena) + Airflow/Step Functions compare + PySpark
concepts (shuffle/broadcast/skew) + healthcare/HIPAA one-liners + rehearse behavioral STAR
stories out loud + prepare your questions. Light SQL practice.
