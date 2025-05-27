In this project I have created a virtual environment for airflow.
Make sure to install dbt-snowflake inside virtual environment.


make sure you do pip install snowflake-connector-python
inside virtual environment

run `pip install pyyaml` in your virtual environment

replace airflow.cfg with 

[smtp]
smtp_host = smtp.gmail.com
smtp_starttls = True
smtp_ssl = False
smtp_port = 587
smtp_user = your_email@gmail.com
smtp_password = your_app_password   ; Not Gmail password — use App Password if 2FA is enabled
smtp_mail_from = your_email@gmail.com