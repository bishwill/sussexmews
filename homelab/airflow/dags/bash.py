from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the DAG
dag = DAG(
    'basic_bash_operator_dag',
    default_args={
        'owner': 'airflow',
        'retries': 1,
    },
    description='A simple BashOperator DAG',
    schedule_interval='@daily',
    start_date=datetime(2024, 12, 23),
    catchup=False,
)

# Define the task
bash_task = BashOperator(
    task_id='run_bash_command',
    bash_command='echo "Hello, you magnificent git!"',
    dag=dag,
)

