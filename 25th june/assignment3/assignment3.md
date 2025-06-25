#  Assignment 3: Trigger Another DAG

##  Objective
Create a parent DAG that triggers a child DAG using Airflow’s `TriggerDagRunOperator`.

---

## 🛠 Features

-  Connects two DAGs in sequence.
-  Passes metadata (`conf`) from parent to child.
-  Demonstrates inter-DAG triggering.
-  Easy to test and extend.

---

##  Folder Structure

![image](https://github.com/user-attachments/assets/d1a2ee88-b4d9-4036-aaf5-d2cc3ff7930e)


---

##  DAG Details

### `parent_dag`

| Task ID            | Description                           |
|--------------------|---------------------------------------|
| `print_hello`      | Logs a greeting message               |
| `trigger_child_dag`| Triggers `child_dag` with a message   |

### `child_dag`

| Task ID     | Description                                 |
|-------------|---------------------------------------------|
| `child_task`| Logs message received from parent DAG       |

---

## code

### parent dag
```
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='parent_dag',
    default_args=default_args,
    description='Parent DAG that triggers another DAG',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
) as dag:

    def greet():
        print(" Hello from parent DAG")

    print_hello = PythonOperator(
        task_id='print_hello',
        python_callable=greet
    )

    trigger_child = TriggerDagRunOperator(
        task_id='trigger_child_dag',
        trigger_dag_id='child_dag',
        conf={"message": "Triggered by parent DAG"}
    )

    print_hello >> trigger_child

```

### child dag

```
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def from_parent(**kwargs):
    conf = kwargs['dag_run'].conf
    message = conf.get("message", "No message received")
    print(f" Received from parent: {message}")

with DAG(
    dag_id='child_dag',
    default_args=default_args,
    description='Child DAG triggered externally',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
) as dag:

    child_task = PythonOperator(
        task_id='child_task',
        python_callable=from_parent,
        provide_context=True
    )

```

## output 

## parent dag
![image](https://github.com/user-attachments/assets/cc8bd37c-468c-4f64-a3d2-ec78486c23cd)

## child dag log
![image](https://github.com/user-attachments/assets/8ddf531a-5ff8-4fc7-8dc6-cab3fa1f7560)

