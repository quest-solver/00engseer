'''Simulated Data Pipeline — ABCD Model'''
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'andre',
    'depends_on_past': False,
    'retries': 0,
    'start_date': datetime(2024, 1, 1)
}

def ingest():
    data = [10, 20, 30, 40, 50]
    print(f"[A - INGEST] Data received: {data}")
    return data

def process():
    data = [10, 20, 30, 40, 50]
    processed = [x * 1.1 for x in data]
    print(f"[B - PROCESS] Data after transformation: {processed}")
    return processed

def validate():
    processed = [11.0, 22.0, 33.0, 44.0, 55.0]
    passed = all(x > 0 for x in processed)
    print(f"[C - VALIDATE] All values positive: {passed}")
    if not passed:
        raise ValueError("Validation failed — negative values detected.")

def report():
    print("[D - REPORT] Pipeline completed. Data is ready for decision-making.")

with DAG(
    dag_id='simulate_data_pipeline',
    description='ABCD control model as a working Airflow pipeline',
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
    tags=['personal', 'phase-1', 'abcd']
) as dag:

    t_ingest = PythonOperator(task_id='ingest', python_callable=ingest)
    t_process = PythonOperator(task_id='process', python_callable=process)
    t_validate = PythonOperator(task_id='validate', python_callable=validate)
    t_report = PythonOperator(task_id='report', python_callable=report)

    t_ingest >> t_process >> t_validate >> t_report