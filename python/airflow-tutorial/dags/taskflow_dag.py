from datetime import datetime, timedelta

from airflow.decorators import dag, task


default_args = {
    "owner": "Finlay",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}


@dag(
    dag_id="python_taskflow_dag_v2",
    default_args=default_args,
    description="A simple python DAG with taskflow API",
    start_date=datetime(2024, 3, 25, 9),
    schedule_interval="@daily",
)
def taskflow_dag():
    @task(multiple_outputs=True)
    def get_name() -> dict[str, str]:
        return {"first_name": "Bob", "last_name": "Smith"}

    @task()
    def get_age() -> int:
        return 25

    @task()
    def print_hello(first_name: str, last_name: str, age: int) -> None:
        print(f"Hello {first_name} {last_name}, you are {age} years old")

    name_dict = get_name()
    age = get_age()
    print_hello(name_dict["first_name"], name_dict["last_name"], age)


taskflow_dag = taskflow_dag()
