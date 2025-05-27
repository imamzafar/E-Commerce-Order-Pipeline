# File: scripts/check_delayed_orders.py

import os
import yaml
import snowflake.connector
import sys

os.environ["SF_OCSP_FAIL_OPEN"] = "true"
os.environ["SF_OCSP_TESTING_ENDPOINT"] = "http://127.0.0.1:12345"

def load_snowflake_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config/snowflake_config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config['snowflake']

def main():
    print("✅ Running Snowflake delayed orders check...")
    print("✅ Python path:", sys.executable)
    print("✅ Snowflake connector version:", snowflake.connector.__version__)

    sf_config = load_snowflake_config()

    try:
        conn = snowflake.connector.connect(
            user=sf_config["user"],
            password=sf_config["password"],
            account=sf_config["account"],
            warehouse=sf_config["warehouse"],
            database=sf_config["database"],
            schema=sf_config["schema"],
            role=sf_config["role"],
            login_timeout=20,
            client_session_keep_alive=False,
            ocsp_fail_open=True
        )
        print("✅ Connected to Snowflake")

        cur = conn.cursor()
        cur.execute("""
            SELECT COUNT(*) 
            FROM ECOMMERCE_DB.ANALYTICS.ORDER_STATUS 
            WHERE FINAL_STATUS = 'DELAYED'
        """)
        result = cur.fetchone()
        print("✅ Query Result:", result)
        cur.close()
        conn.close()

        if result[0] > 0:
            raise Exception(f"{result[0]} delayed orders found.")

    except Exception as e:
        print("❌ Error:", e)
        sys.exit(1)  # non-zero exit = task fail

if __name__ == "__main__":
    main()
