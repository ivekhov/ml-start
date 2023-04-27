from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime, timedelta


def push(ti):
    ti.xcom_push(
        key='sample_xcom_key',
        value='xcom test'
        )


def pull(ti):
    xcom_test = ti.xcom_pull(
        key='sample_xcom_key',
        task_ids='push_xcom'
        )
    print(xcom_test)


with DAG(
    'hw_9_i-vekhov',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='hw_9_i-vekhov',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 3, 1),
    catchup=False,
    tags=['hw_9_i-vekhov'],
) as dag:
    a1 = PythonOperator(
        task_id='push_xcom',
        python_callable=push
    )
    a2 = PythonOperator(
        task_id='pull_xcom',
        python_callable=pull
    )
    a1 >> a2
