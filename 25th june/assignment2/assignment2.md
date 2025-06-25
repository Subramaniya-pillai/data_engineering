#  Assignment 2: Data Quality Validation

##  Objective
Build an Apache Airflow DAG that validates the structure and content of `orders.csv` before processing.

---

## 🛠️ Features

-  Reads incoming `orders.csv` file.
-  Validates required columns.
-  Checks for nulls in critical fields.
-  Uses branching to stop the DAG on validation failure.
-  Prints a summary only if validation passes.

---

##  Folder Structure

![image](https://github.com/user-attachments/assets/9be559dd-0f44-4456-8cbe-904ec4bdd68e)

## code

```
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import pandas as pd
import os

#  File path inside Docker
ORDERS_FILE = '/opt/airflow/dags/assignment2/data/orders.csv'
REQUIRED_COLUMNS = ['order_id', 'customer_name', 'amount']
MANDATORY_FIELDS = ['order_id', 'amount']

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='data_quality_validation',
    default_args=default_args,
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
    description='Validate incoming orders.csv before processing',
) as dag:

    def read_orders():
        print(f"Reading {ORDERS_FILE}")
        df = pd.read_csv(ORDERS_FILE)
        print(df.head())

    def validate_structure():
        df = pd.read_csv(ORDERS_FILE)
        missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")
        print(" All required columns present")

    def check_nulls_and_branch(**context):
        df = pd.read_csv(ORDERS_FILE)
        nulls_found = df[MANDATORY_FIELDS].isnull().any().any()
        print("Null check:", nulls_found)
        return 'summarize_data' if not nulls_found else 'fail_task'

    def summarize():
        df = pd.read_csv(ORDERS_FILE)
        total_orders = len(df)
        total_amount = df['amount'].sum()
        print(f"Total orders: {total_orders}")
        print(f"Total amount: ₹{total_amount}")

    read_task = PythonOperator(
        task_id='read_orders',
        python_callable=read_orders
    )

    validate_task = PythonOperator(
        task_id='validate_columns',
        python_callable=validate_structure
    )

    branching = BranchPythonOperator(
        task_id='check_nulls',
        python_callable=check_nulls_and_branch,
        provide_context=True
    )

    summarize_task = PythonOperator(
        task_id='summarize_data',
        python_callable=summarize
    )

    fail_task = DummyOperator(
        task_id='fail_task'
    )

    end = DummyOperator(
        task_id='end',
        trigger_rule='none_failed_min_one_success'
    )

    # DAG flow
    read_task >> validate_task >> branching
    branching >> summarize_task >> end
    branching >> fail_task >> end

```


## output

### summary in the logs
![image](https://github.com/user-attachments/assets/d2ff039e-5337-4e20-865e-0532f4f6262c)

### 
![image](https://github.com/user-attachments/assets/43f5e1c9-f267-4821-8e2e-8faa148566c9)
