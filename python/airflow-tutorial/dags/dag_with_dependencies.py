from datetime import datetime, timedelta
import pandas as pd

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "Finlay",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


def get_pandas_version() -> str:
    return pd.__version__


with DAG(
    dag_id="python_ext_deps_dag_v1",
    default_args=default_args,
    description="A simple python DAG with external dependencies",
    start_date=datetime(2024, 3, 25, 9),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    get_pandas_version = PythonOperator(
        task_id="pandas_version", python_callable=get_pandas_version
    )

    get_pandas_version
