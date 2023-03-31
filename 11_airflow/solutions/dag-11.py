from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.postgres.hooks.postgres import PostgresHook


def find_active_user():
    postgres = PostgresHook(postgres_conn_id="startml_feed")
    with postgres.get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            SELECT
                user_id
                , COUNT(*)
            FROM feed_action
            WHERE action = 'like'
            GROUP BY user_id
            ORDER BY COUNT(*) DESC
            LIMIT 1
            """)
            return cursor.fetchone()


with DAG(
    'hw_11_i-vekhov',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),  # timedelta из пакета datetime
    },
    description='hw_11_i-vekhov',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 3, 29),
    catchup=False,
    tags=['hw_11_i-vekhov'],
) as dag:
    select_active_user = PythonOperator(
        task_id='select_active_user',
        python_callable=find_active_user
    )
