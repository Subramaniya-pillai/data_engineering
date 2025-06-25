from airflow import DAG
from datetime import datetime
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator

dag1 = DAG(
    'email_notifications',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    default_args={
        'email_on_failure': True,
        'email': [Variable.get("alert_email", default_var="admin@example.com")]
    }
)

def always_success():
    return True

task1 = PythonOperator(task_id='task1', python_callable=always_success, dag=dag1)
task2 = PythonOperator(task_id='task2', python_callable=always_success, dag=dag1)

success_email = EmailOperator(
    task_id='send_success_email',
    to=Variable.get("alert_email", default_var="admin@example.com"),
    subject='All Tasks Successful',
    html_content='All tasks completed successfully.',
    trigger_rule='all_success',
    dag=dag1
)

task1 >> task2 >> success_email