from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "Finlay",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


def print_hello(age: int, ti) -> None:
    name = ti.xcom_pull(task_ids="get_name_task")
    print(f"Hello {name}, you are {age} years old")


def get_name() -> str:
    return "Bob"


with DAG(
    dag_id="python_xcomms_dag_v2",
    default_args=default_args,
    description="A simple python DAG with xcomms to pass values between tasks",
    start_date=datetime(2024, 3, 25, 9),
    schedule_interval="@daily",
) as dag:
    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=print_hello,
        # op_kwargs={"name": "Bob", "age": 25},
        op_kwargs={"age": 25},
    )

    get_name_task = PythonOperator(
        task_id="get_name_task",
        python_callable=get_name,
    )

    get_name_task >> hello_task
