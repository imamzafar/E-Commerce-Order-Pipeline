# Your Project Story — E-Commerce Order Pipeline (talk about THIS)

This is your strongest asset. It hits: pipelines, dbt, Airflow, layered modeling,
and data quality — 5 of the JD bullets. Learn to narrate it in ~90 seconds (STAR).

## The 90-second narration (memorize the shape, not the words)

**Situation/Task:** "I built an end-to-end e-commerce order pipeline to monitor order
fulfillment and automatically flag delayed shipments — the kind of operational data
product a business team relies on daily."

**Action — the architecture (say it as layers):**
- **Ingestion:** raw customer, order, and shipment data landing in a `raw` schema
  (I generated realistic dummy data with a Python/pandas notebook to simulate source loads).
- **Transformation with dbt:** a layered model design —
  - **staging** models (`stg_customers`, `stg_orders`, `stg_shipments`) that clean and
    standardize each source, materialized as views;
  - a **marts** model (`order_status`) that joins the three and applies business logic —
    `DATEDIFF` between shipped and delivered timestamps, and a `CASE` rule that marks an
    order `DELAYED` when it's shipped but delivery took more than 48 hours.
- **Orchestration with Airflow:** an hourly DAG with two tasks wired `dbt_run >> check_orders`
  — first `dbt run` rebuilds the models, then a Python task queries the mart.
- **Data quality / alerting:** the check task counts `DELAYED` orders and **fails the task
  with a non-zero exit** if any exist, which triggers Airflow's `email_on_failure` to alert me.

**Result:** "A self-service, scheduled pipeline where business logic lives in version-controlled
dbt models, and operational anomalies page a human automatically — no manual monitoring."

## Design decisions you can defend (they WILL probe)
- **Why staging → marts layering?** Separation of concerns: staging isolates source-specific
  cleaning so downstream models don't break when a source changes; marts hold business logic
  reusable across consumers. (This is the "reusable transformation framework" bullet in their JD.)
- **Why views vs tables?** Views = always-fresh, no storage, fine at this data size. I'd switch
  marts to **incremental tables** as volume grows (see gaps doc — great thing to volunteer).
- **Why fail the DAG on delayed orders?** Turning a data condition into a pipeline signal =
  observability. It's the same instinct as a dbt test or a data-quality gate.
- **Idempotency:** dbt `run` rebuilds deterministically from source; the check is read-only.

## Honest self-critique (bring these up BEFORE they do — shows seniority)
- Hardcoded absolute paths in the DAG's bash commands → should be Airflow Variables / env vars.
- Snowflake creds in a YAML file → should be a secrets manager / Airflow Connections.
- No dbt tests yet (`not_null`, `unique`, `relationships`) → would add to `schema.yml`.
- Business logic (48h, 'DELAYED') hardcoded in SQL → would parameterize via dbt vars.
- Using `BashOperator` to call dbt → would move to `DbtCloudRunJobOperator` / Cosmos.

## The pivot sentence (Snowflake → their AWS stack)
"I implemented the warehouse layer on Snowflake, but the pattern is portable: swap Snowflake
for **Iceberg tables on S3**, the dbt adapter to **dbt-athena** (or dbt-glue), and the Python
check to a **Glue/Athena query** — the layered dbt design and orchestration logic carry over
unchanged. That's exactly the 'modernize legacy workloads onto Iceberg' work in your JD."
