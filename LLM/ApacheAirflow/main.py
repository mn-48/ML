from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# একটি ফাংশন যা টাস্ক হিসেবে চলবে
def print_hello():
    print("Hello, Apache Airflow!")

# DAG কনফিগারেশন
default_args = {
    'owner': 'nazmul',
    'start_date': datetime(2025, 2, 1),
}

dag = DAG('hello_airflow', default_args=default_args, schedule_interval='@daily')

# Python টাস্ক তৈরি করা
hello_task = PythonOperator(
    task_id='print_hello_task',
    python_callable=print_hello,
    dag=dag
)
