# Assignment 3 – Branching DAG in Apache Airflow

This DAG demonstrates the use of `BranchPythonOperator` to decide task execution based on the presence of a file. If the file exists, it is processed. If not, a warning is logged.

---

##  Folder Structure
![image](https://github.com/user-attachments/assets/f81d4195-10f2-4c86-b000-c9fd77a1a9de)


---

## 🧠 Use Case

- **Purpose**: Check if `input.csv` exists.
- **Branching Logic**:
  - If the file exists → process it.
  - If not → log a missing file message.
- **Final Task** (`end`) runs regardless of the path taken.

---

## 🔧 DAG Configuration

| Task ID           | Operator               | Description                       |
|------------------|------------------------|-----------------------------------|
| `check_file_branch` | BranchPythonOperator | Checks if file exists             |
| `process_file`      | PythonOperator        | Reads and prints file content     |
| `file_missing`      | PythonOperator        | Logs missing file message         |
| `end`               | EmptyOperator         | Final task that always runs       |

---

##  Sample CSV (input.csv)

```csv
id,name,score
1,Alice,87
2,Bob,91
3,Charlie,78
4,David,85
5,Eve,92

```


## code 
```
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago
from airflow.utils.trigger_rule import TriggerRule
import os
import pandas as pd

# Base paths
BASE_PATH = os.path.join(os.environ["AIRFLOW_HOME"], "dags", "assignment-3")
FILE_PATH = os.path.join(BASE_PATH, "data", "input.csv")

# DAG definition
default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    dag_id='branching_file_check_dag',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
    description='Branching DAG to process a file if exists, else handle missing'
) as dag:

    def decide_branch():
        if os.path.exists(FILE_PATH):
            return 'process_file'
        else:
            return 'file_missing'

    def process_file():
        df = pd.read_csv(FILE_PATH)
        print("Processing file:")
        print(df.head())

    def handle_missing_file():
        print(f"File not found at {FILE_PATH}")

    check_file_branch = BranchPythonOperator(
        task_id='check_file_branch',
        python_callable=decide_branch
    )

    process_file_task = PythonOperator(
        task_id='process_file',
        python_callable=process_file
    )

    file_missing = PythonOperator(
        task_id='file_missing',
        python_callable=handle_missing_file
    )

    end = EmptyOperator(
        task_id='end',
        trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS
    )

    # DAG flow
    check_file_branch >> [process_file_task, file_missing]
    process_file_task >> end
    file_missing >> end

```


![image](https://github.com/user-attachments/assets/5b13059d-2aa3-43c4-a97d-d7fe5b9d9b97)
