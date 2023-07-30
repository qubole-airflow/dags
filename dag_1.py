from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

dag = DAG('my_first_dag', description='A simple tutorial DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2023, 7, 30), catchup=False)

dummy_task = DummyOperator(task_id='dummy_task', retries=3, dag=dag)