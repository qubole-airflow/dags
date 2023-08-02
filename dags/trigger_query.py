from airflow import DAG
from airflow.contrib.operators.qubole_operator import QuboleOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 1),
    'email': ['krishna@galtsudoers.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('qubole_show_tables', default_args=default_args, schedule_interval=timedelta(minutes=30))

t1 = QuboleOperator(
    task_id='show_tables',
    command_type='hivecmd',
    query="SHOW tables;",
    cluster_label='hadoop',
    fetch_logs=True,
    qubole_conn_id="qubole_default",
    dag=dag)

t1
