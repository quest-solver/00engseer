from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("DAG is alive. Pipeline logic goes here.")

with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["learning", "phase-1"],
) as dag:

    task_hello = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )