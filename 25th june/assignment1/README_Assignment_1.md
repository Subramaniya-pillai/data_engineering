
#  Assignment 1: File Sensor Pipeline

##  Objective
Build an Apache Airflow DAG that waits for a CSV file to arrive, processes its content, and then moves the file to an archive directory.

---

## 🛠 Features

-  Uses `FileSensor` to detect incoming files.
-  Validates file existence before processing.
-  Reads and prints file structure (rows, columns).
-  Moves processed file to an archive folder.
-  Handles missing files with graceful failure using a custom filesystem connection.

---

##  Directory Structure

```
assignment1/
├── file_sensor_dag.py
└── data/
    ├── incoming/
    │   └── report.csv        #  input file here
    └── archive/              # Processed files will be moved here
```

---



##  DAG Logic

| Task ID           | Description                                                |
|------------------|------------------------------------------------------------|
| `wait_for_file`   | Waits for `report.csv` to appear in the `incoming/` folder |
| `process_csv`     | Reads the file and logs number of rows & columns           |
| `move_to_archive` | Moves file to `archive/` folder                            |

---


## code

```
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import pandas as pd
import shutil
import os

#  Container paths (not Windows paths)
BASE_PATH = '/opt/airflow/dags'
INCOMING_FILE = f'{BASE_PATH}/assignment1/data/incoming/report.csv'
ARCHIVE_FILE = f'{BASE_PATH}/assignment1/data/archive/report.csv'

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

def process_file():
    print(f"Reading file: {INCOMING_FILE}")
    df = pd.read_csv(INCOMING_FILE)
    print(f"File has {df.shape[0]} rows and {df.shape[1]} columns.")
    print("Column names:", df.columns.tolist())

def archive_file():
    print(f"Archiving file to: {ARCHIVE_FILE}")
    shutil.move(INCOMING_FILE, ARCHIVE_FILE)
    print("File moved to archive.")

with DAG(
    dag_id='file_sensor_pipeline',
    default_args=default_args,
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    description='DAG that waits for a file, processes it, and archives it'
) as dag:

    wait_for_file = FileSensor(
        task_id='wait_for_file',
        filepath=INCOMING_FILE,
        poke_interval=30,
        timeout=600,
        mode='poke',
        soft_fail=False
    )

    process_csv = PythonOperator(
        task_id='process_csv',
        python_callable=process_file
    )

    move_to_archive = PythonOperator(
        task_id='move_to_archive',
        python_callable=archive_file
    )

    wait_for_file >> process_csv >> move_to_archive

```

## output

![image](https://github.com/user-attachments/assets/f1d50b0a-6bc4-462b-ac91-12784978a9cd)


