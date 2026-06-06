from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="employee_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="echo Extracting Data"
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="echo Transforming Data"
    )

    load = BashOperator(
        task_id="load",
        bash_command="echo Loading Data"
    )

    extract >> transform >> load