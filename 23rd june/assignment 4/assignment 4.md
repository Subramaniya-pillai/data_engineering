# Assignment 4: Watch and Process CSV Files using Apache Airflow

##  Objective

Create an Airflow DAG that:
- Monitors a folder for new CSV files
- Reads and analyzes the first available file
- Logs basic statistics (row count, column count, missing values)
- Copies the processed file to an archive directory without deleting the original

---

##  Project Structure

![image](https://github.com/user-attachments/assets/e896c2d8-3fe5-4281-9067-36fd86cb6996)



---

##  DAG Details

- **DAG ID**: `watch_and_process_csv`
- **Schedule**: Hourly (`@hourly`)
- **Tasks**:
  1. `find_csv_file` – Find the first `.csv` in the `data/` folder
  2. `process_csv` – Read the file and print:
     - Filename
     - Row and column counts
     - Count of missing values per column
  3. `copy_csv` – Copy the processed file to the `processed/` folder

---


## code

```
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import pandas as pd
import os
import shutil

BASE_DIR = os.path.join(os.environ['AIRFLOW_HOME'], 'dags', 'assignment-4')
DATA_DIR = os.path.join(BASE_DIR, 'data')
PROCESSED_DIR = os.path.join(BASE_DIR, 'processed')

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

def find_new_csv():
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
    if not files:
        raise FileNotFoundError("No new CSV files found.")
    return files[0]

def process_csv(**context):
    filename = context['ti'].xcom_pull(task_ids='find_csv_file')
    path = os.path.join(DATA_DIR, filename)
    df = pd.read_csv(path)
    print("File:", filename)
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Missing values:\n", df.isnull().sum())

def copy_to_processed(**context):
    filename = context['ti'].xcom_pull(task_ids='find_csv_file')
    src = os.path.join(DATA_DIR, filename)
    dst = os.path.join(PROCESSED_DIR, filename)
    shutil.copy(src, dst)  # 
    print(f"Copied {filename} to processed/")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='watch_and_process_csv',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval='@hourly',
    catchup=False
)

t1 = PythonOperator(
    task_id='find_csv_file',
    python_callable=find_new_csv,
    dag=dag
)

t2 = PythonOperator(
    task_id='process_csv',
    python_callable=process_csv,
    provide_context=True,
    dag=dag
)

t3 = PythonOperator(
    task_id='copy_csv',
    python_callable=copy_to_processed,
    provide_context=True,
    dag=dag
)

t1 >> t2 >> t3

```


![image](https://github.com/user-attachments/assets/dfb475bb-ef05-44b8-9cf4-71f483da5a5e)
