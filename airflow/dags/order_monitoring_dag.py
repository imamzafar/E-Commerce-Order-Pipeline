from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago

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