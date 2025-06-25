#  Assignment 4: Retry and Timeout Handling

##  Objective
Create an Airflow DAG that simulates a long-running task with retries, timeout enforcement, and clear logging.

---

##  Features

-  Task-level execution timeout (15 seconds)
-  Retries on failure (2 retries)
-  Exponential backoff via `retry_delay`
-  Logs duration and retry attempts
-  Final log task runs regardless of failure

---

##  Folder Structure

![image](https://github.com/user-attachments/assets/f8dcae4b-5f42-4ab3-9ca5-1d8d41cd5e40)


---

##  DAG Tasks

| Task ID         | Description                                           |
|-----------------|-------------------------------------------------------|
| `simulate_work` | Sleeps randomly (5–20 sec); fails if >15 sec         |
| `final_log`     | Logs that the DAG finished (even if prior task failed)|

---

## code/retry_timeout_dag.py

```
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import time
import random

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(seconds=10)
}

with DAG(
    dag_id='retry_timeout_dag',
    default_args=default_args,
    description='DAG with retry and timeout handling',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False
) as dag:

    def simulate_work():
        print(" Simulating long-running task...")
        delay = random.randint(5, 20)  # simulate variable execution time
        print(f" Sleeping for {delay} seconds")
        time.sleep(delay)
        if delay > 15:
            raise TimeoutError(" Simulated timeout exceeded!")
        print(" Task completed successfully.")

    def log_final_status():
        print(" Final log: DAG completed (check for retries or failure).")

    simulate_task = PythonOperator(
        task_id='simulate_work',
        python_callable=simulate_work,
        execution_timeout=timedelta(seconds=15)
    )

    final_log = PythonOperator(
        task_id='final_log',
        python_callable=log_final_status,
        trigger_rule='all_done'  # Runs even if previous task fails
    )

    simulate_task >> final_log

```

## output

![image](https://github.com/user-attachments/assets/ba143afe-bf08-4057-9348-f247961720fe)

---
### stimulate work log

![image](https://github.com/user-attachments/assets/25207d94-4129-4d48-8d6b-0c08168cc42f)

---
### final log

![image](https://github.com/user-attachments/assets/72f81ed5-2934-4bab-95fd-d5ad2dcbdeb4)

---
