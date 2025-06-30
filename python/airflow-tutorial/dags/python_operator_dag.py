from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "Finlay",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


def print_hello(name: str, age: int) -> None:
    print(f"Hello {name}, you are {age} years old")


with DAG(
    dag_id="python_dag_v2",
    default_args=default_args,
    description="A simple python DAG",
    start_date=datetime(2024, 3, 26, 9),
    schedule_interval="@daily",
) as dag:
    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=print_hello,
        op_kwargs={"name": "Bob", "age": 25},
    )

    hello_task
