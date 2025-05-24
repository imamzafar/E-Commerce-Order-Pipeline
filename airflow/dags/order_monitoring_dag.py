import yaml
import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago
import snowflake.connector

# Load Snowflake config from YAML
def load_snowflake_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'snowflake_config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config['snowflake']

def check_delayed_orders():
    sf_config = load_snowflake_config()

    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=sf_config["user"],
        password=sf_config["password"],
        account=sf_config["account"],
        warehouse=sf_config["warehouse"],
        database=sf_config["database"],
        schema=sf_config["schema"],
        role=sf_config["role"]
    )

    cur = conn.cursor()
    cur.execute("""
        SELECT COUNT(*) 
        FROM orders 
        WHERE status = 'Delayed' AND updated_at >= DATEADD(hour, -1, CURRENT_TIMESTAMP)
    """)
    result = cur.fetchone()
    delayed_count = result[0]
    cur.close()
    conn.close()

    if delayed_count > 0:
        raise ValueError(f"{delayed_count} delayed orders found.")  # Triggers failure & email alert



with DAG(
    dag_id='order_monitoring_dag1',
    schedule_interval='@hourly',
    start_date=days_ago(1),
    catchup=False
) as dag:

    dbt_run = BashOperator(
        task_id='run_dbt_models',
        bash_command='source "/Users/zafarimam/Documents/E-Commerce Order Pipeline/airflow_venv_39/bin/activate" && cd "/Users/zafarimam/Documents/E-Commerce Order Pipeline/dbt_ecommerce" && dbt run'
    )

    alert = EmailOperator(
        task_id='email_delayed_orders',
        to='ops@example.com',
        subject='[ALERT] Delayed Orders Detected',
        html_content='One or more orders are delayed in shipping. Please check the dashboard.'
    )

    dbt_run >> alert