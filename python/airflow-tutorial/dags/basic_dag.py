from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Finlay",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="basic_dag_v2",
    default_args=default_args,
    description="A simple DAG",
    start_date=datetime(2024, 1, 1, 9),
    schedule_interval="@daily",
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'Hello from Task 1'",
    )

    task2 = BashOperator(
        task_id="task2",
        bash_command="echo 'Hello from Task 2, downstream from Task 1'",
    )

    task3 = BashOperator(
        task_id="task3",
        bash_command="echo 'Hello from Task 3, downstream from Task 1 as well '",
    )

    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    task1 >> [task2, task3]
