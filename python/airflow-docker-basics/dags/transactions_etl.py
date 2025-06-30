from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "Finlay",
    # "depends_on_past": False,
    # "email": ["airflow@example.com"],
    # "email_on_failure": False,
    # "email_on_retry": False,
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="transactions_etl",
    default_args=default_args,
    description="ETL for transactions data",
    # start_date=datetime(2024, 3, 26, 9),
    start_date=days_ago(1),
    schedule_interval="@daily",
    # schedule_interval=timedelta(days=1),
) as dag:
    pass
