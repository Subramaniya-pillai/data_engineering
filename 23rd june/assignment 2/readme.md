# Assignment 2: Daily Sales Report (Airflow DAG)

##  Objective
Automate a daily sales report using Apache Airflow. The DAG:
- Reads a `sales.csv` file
- Groups data by product category
- Calculates total sales per category
- Writes the summary to a new CSV file
- Archives the original file after processing

---

##  Schedule
- Runs **daily at 6 AM**
- Includes a timeout: **Fails** if any task runs over **5 minutes**

---

##  Folder Structure

![image](https://github.com/user-attachments/assets/ff8db9f5-3f1c-4cbb-9724-a896ca4e5fd8)

## code
```
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import pandas as pd
import os
import shutil

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='daily_sales_report',
    default_args=default_args,
    description='Generate daily sales summary report',
    schedule_interval='0 6 * * *',  # every day at 6 AM
    start_date=days_ago(1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=5)
)

BASE_PATH = os.path.join(os.environ["AIRFLOW_HOME"], "dags", "assignment-2")
DATA_PATH = os.path.join(BASE_PATH, "data", "sales.csv")
SUMMARY_PATH = os.path.join(BASE_PATH, "data", "sales_summary.csv")
ARCHIVE_PATH = os.path.join(BASE_PATH, "archive", "sales.csv")

def read_and_summarize():
    df = pd.read_csv(DATA_PATH)
    summary = df.groupby("category")["amount"].sum().reset_index()
    summary.to_csv(SUMMARY_PATH, index=False)
    print("Sales Summary:\n", summary)

def archive_file():
    os.makedirs(os.path.dirname(ARCHIVE_PATH), exist_ok=True)
    shutil.move(DATA_PATH, ARCHIVE_PATH)
    print(f"Moved sales.csv to archive")

task_summarize = PythonOperator(
    task_id='summarize_sales',
    python_callable=read_and_summarize,
    dag=dag
)

task_archive = PythonOperator(
    task_id='archive_sales_file',
    python_callable=archive_file,
    dag=dag
)

task_summarize >> task_archive

```

## output

![image](https://github.com/user-attachments/assets/2b804dd0-43d5-4736-85fc-fb543266012a)

## logs

![image](https://github.com/user-attachments/assets/1f72df72-07af-45ba-b07d-99d389f2c5ae)

