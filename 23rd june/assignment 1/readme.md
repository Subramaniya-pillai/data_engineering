#  Assignment 1: CSV to Summary DAG

This  contains an Apache Airflow DAG that performs a simple data validation and summarization pipeline using a CSV file.

---

##  Objective

Create an Airflow DAG that:
1. Checks if `customers.csv` exists.
2. Reads the CSV file and counts the number of rows.
3. Logs the row count.
4. *(Bonus)* Sends a Bash message if the row count is greater than 100.

---

##  Folder Structure

![image](https://github.com/user-attachments/assets/355e8434-f186-4aea-8792-38e763955c8f)



## docker-compose.yml
```python

version: '3'

services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres_db:/var/lib/postgresql/data

  webserver:
    image: apache/airflow:2.7.1
    environment:
      AIRFLOW_CORE_EXECUTOR: SequentialExecutor
      AIRFLOW__CORE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      AIRFLOW_CORE_FERNET_KEY: 'k305c0kb68MevNWLSWVN-IZF_d6eNbxa21aGnnKcohs='
      AIRFLOW_CORE_DAGS_ARE_PAUSED_AT_CREATION: 'true'
      AIRFLOW_CORE_LOAD_EXAMPLES: 'false'
      AIRFLOW__WEBSERVER__SECRET_KEY: 'k305c0kb68MevNWLSWVN-IZF_d6eNbxa21aGnnKcohs='
    depends_on:
      - postgres
    ports:
      - "8080:8080"
    volumes:
      - ./dags:/opt/airflow/dags
      - ./dags/data:/opt/airflow/data 
    command: webserver

  scheduler:
    image: apache/airflow:2.7.1
    depends_on:
      - postgres
    environment:
      AIRFLOW_CORE_EXECUTOR: SequentialExecutor
      AIRFLOW__CORE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      AIRFLOW_CORE_FERNET_KEY: 'k305c0kb68MevNWLSWVN-IZF_d6eNbxa21aGnnKcohs='
      AIRFLOW__WEBSERVER__SECRET_KEY: 'k305c0kb68MevNWLSWVN-IZF_d6eNbxa21aGnnKcohs='
    volumes:
      - ./dags:/opt/airflow/dags
      - ./dags/data:/opt/airflow/data
    command: scheduler

  airflow-init:
    image: apache/airflow:2.7.1
    depends_on:
      - postgres
    environment:
      AIRFLOW__CORE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      AIRFLOW__CORE__EXECUTOR: SequentialExecutor
      _AIRFLOW_DB_UPGRADE: 'true'
      _AIRFLOW_WWW_USER_CREATE: 'true'
      _AIRFLOW_WWW_USER_USERNAME: airflow
      _AIRFLOW_WWW_USER_PASSWORD: airflow
    volumes:
      - ./dags:/opt/airflow/dags
      - ./dags/data:/opt/airflow/data
    entrypoint: >
      bash -c "airflow db migrate && airflow users create
      --username airflow --password airflow --firstname Air --lastname Flow
      --role Admin --email airflow@example.com"

volumes:
  postgres_db:

```
## output:
![image](https://github.com/user-attachments/assets/8b6b5aa9-89ae-45ca-8b9c-1bd28ee78005)
