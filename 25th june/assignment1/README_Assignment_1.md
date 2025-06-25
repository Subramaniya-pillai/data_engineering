
# 📂 Assignment 1: File Sensor Pipeline

## 🎯 Objective
Build an Apache Airflow DAG that waits for a CSV file to arrive, processes its content, and then moves the file to an archive directory.

---

## 🛠️ Features

- ⏳ Uses `FileSensor` to detect incoming files.
- ✅ Validates file existence before processing.
- 📊 Reads and prints file structure (rows, columns).
- 📁 Moves processed file to an archive folder.
- 🔒 Handles missing files with graceful failure using a custom filesystem connection.

---

## 📁 Directory Structure

```
assignment1/
├── file_sensor_dag.py
└── data/
    ├── incoming/
    │   └── report.csv        # Place your input file here
    └── archive/              # Processed files will be moved here
```

---

## 🔗 Airflow Connection Setup

Create a connection in Airflow named `fs_default`:

1. Go to **Admin → Connections → Add (+)**  
2. Fill in:
   - **Conn Id**: `fs_default`
   - **Conn Type**: `File (path)`
   - **Extra**:
     ```json
     {"path": "/opt/airflow/dags"}
     ```
3. Save.

---

## 🧠 DAG Logic

| Task ID           | Description                                                |
|------------------|------------------------------------------------------------|
| `wait_for_file`   | Waits for `report.csv` to appear in the `incoming/` folder |
| `process_csv`     | Reads the file and logs number of rows & columns           |
| `move_to_archive` | Moves file to `archive/` folder                            |

---

## 🧪 Testing the DAG

1. Place your `report.csv` file in:
   ```
   D:\airflow\dags\assignment1\data\incoming\report.csv
   ```
2. Trigger the DAG in the Airflow UI.
3. Verify logs and check if the file is moved to the archive folder.

---

## 🐳 Docker Volume (from `docker-compose.yml`)

Make sure your `docker-compose.yml` includes:

```yaml
volumes:
  - D:\airflow\dags:/opt/airflow/dags
```

---
