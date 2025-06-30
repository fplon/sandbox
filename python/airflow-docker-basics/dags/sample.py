from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "hello_world",
    default_args=default_args,
    description="A simple hello world DAG",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    tags=["example"],
)

t1 = DummyOperator(
    task_id="start",
    dag=dag,
)

t2 = DummyOperator(
    task_id="end",
    dag=dag,
)

t1 >> t2
