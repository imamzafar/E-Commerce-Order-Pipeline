# import os
# import yaml
# import sys
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
# import snowflake.connector
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'email': ['imamzafar100@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

# # Load Snowflake config from YAML
# def load_snowflake_config():
#     print("✅ Airflow Python path:", sys.executable)
#     print("✅ Snowflake connector version:", snowflake.connector.__version__)
#     print("✅ ENV:", os.environ)

#     config_path = os.path.join(os.path.dirname(__file__), 'config', 'snowflake_config.yaml')
#     with open(config_path, 'r') as file:
#         config = yaml.safe_load(file)
#     return config['snowflake']

# def check_delayed_orders():
#     print('inside check_delayed_orders15')
#     sf_config = load_snowflake_config()
#     print(f"account: {sf_config['account']}")
#     # os.environ["SF_OCSP_TESTING_ENDPOINT"] = "http://127.0.0.1:12345"

#     try:
#         print("✅ Attempting connection to Snowflake...")
        
#         conn = snowflake.connector.connect(
#             user=sf_config["user"],
#             password=sf_config["password"],
#             account=sf_config["account"],
#             warehouse=sf_config["warehouse"],
#             database=sf_config["database"],
#             schema=sf_config["schema"],
#             role=sf_config["role"],
#             login_timeout=20,
#             client_session_keep_alive=False,
#             ocsp_fail_open=True,  # ✅ Already present, helps
#         )
#         print("✅ Connected to Snowflake")
        
#         cur = conn.cursor()
#         cur.execute("""
#             SELECT COUNT(*) 
#             FROM ECOMMERCE_DB.ANALYTICS.ORDER_STATUS 
#             WHERE FINAL_STATUS = 'DELAYED'
#         """)
#         result = cur.fetchone()
#         print("✅ Query Result:", result)
#         cur.close()
#         conn.close()

#         if result[0] > 0:
#             raise ValueError(f"{result[0]} delayed orders found.")
#     except Exception as e:
#         print("❌ Exception while connecting to Snowflake:")
#         print(repr(e))
#         raise

with DAG(
    dag_id='order_monitoring_dag16',
    default_args=default_args,
    schedule_interval='@hourly',
    start_date=days_ago(1),
    catchup=False
) as dag:

    dbt_run = BashOperator(
        task_id='run_dbt_models',
        bash_command='source "/Users/zafarimam/Documents/E-Commerce Order Pipeline/airflow_venv_39/bin/activate" && cd "/Users/zafarimam/Documents/E-Commerce Order Pipeline/dbt_ecommerce" && dbt run'
    )

    check_orders = BashOperator(
        task_id='check_delayed_orders',
        bash_command='source "/Users/zafarimam/Documents/E-Commerce Order Pipeline/airflow_venv_39/bin/activate" && python "/Users/zafarimam/Documents/E-Commerce Order Pipeline/airflow_project/dags/utils/check_delayed_orders.py"'
    )

    dbt_run >> check_orders