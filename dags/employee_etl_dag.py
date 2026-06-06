from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="employee_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    test_task = BashOperator(
        task_id="test_task",
        bash_command="echo 'Airflow DAG Working Successfully'"
    )