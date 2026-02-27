'''Learning Progress Tracker DAG'''
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'andre',
    'depends_on_past': False,
    'retries': 0,
    'start_date': datetime(2024, 1, 1)
}

def read_career_file():
    with open('/opt/airflow/dags/career_path_master.txt', 'r') as f:
        content = f.read()
    print("File read successfully.")
    print(f"Total characters: {len(content)}")
    return content

def count_progress():
    with open('/opt/airflow/dags/career_path_master.txt', 'r') as f:
        lines = f.readlines()
    done = sum(1 for line in lines if '[DONE]' in line)
    pending = sum(1 for line in lines if '[ ]' in line)
    print(f"--- LEARNING PROGRESS ---")
    print(f"Completed: {done}")
    print(f"Pending:   {pending}")
    print(f"Progress:  {round(done/(done+pending)*100)}%" if (done+pending) > 0 else "No items found.")

with DAG(
    dag_id='check_learning_progress',
    description='Reads career_path_master and reports progress',
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
    tags=['personal', 'phase-1']
) as dag:

    t0 = PythonOperator(
        task_id='read_file',
        python_callable=read_career_file
    )

    t1 = PythonOperator(
        task_id='count_progress',
        python_callable=count_progress
    )

    t0 >> t1