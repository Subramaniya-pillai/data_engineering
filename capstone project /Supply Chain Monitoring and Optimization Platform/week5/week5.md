#  Week 5 – CI/CD Automation for Delay Analysis Script

##  Objective
Automate the execution of the supply chain delay analysis script using GitHub Actions and generate output CSV upon each push to the repository.

---

##  Tools Used
- GitHub Actions (CI/CD)
- Python 3.10
- Pandas, Matplotlib
- `actions/setup-python@v4`, `actions/upload-artifact@v4`

---

##  File Structure
data_engineering/
│

├── delay_analysis.py # Python script for delay processing

├── supply_chain_orders.csv # Input data for delay tracking

└── .github/

└── workflows/

└── delay_analysis.yml # GitHub Actions workflow file

---


---

##  Steps Automated

###  1. Trigger on Push
The pipeline runs automatically when code is pushed to the repository (`main` branch).

###  2. Setup Python 3.10
Installs Python version `3.10.x` to run the script.

###  3. Install Dependencies
Installs required packages (e.g., `pandas`, `matplotlib`).

###  4. Execute Script
Runs `delay_analysis.py` which:
- Reads `supply_chain_orders.csv`
- Calculates delay in days
- Generates a summary grouped by `supplier_id`
- Saves the result to a new timestamped CSV

###  5. Upload Output
The output file (e.g., `delayed_summary_20250701_090413.csv`) is uploaded as an artifact to GitHub Actions.

---

##  Sample YAML (delay_analysis.yml)

```yaml
name: Delay Analysis CI

on:
  push:
    branches:
      - main

jobs:
  run-delay-analysis:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repo
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install pandas matplotlib

    - name: Run Delay Analysis
      run: python delay_analysis.py

    - name: Upload Output CSV
      uses: actions/upload-artifact@v4
      with:
        name: delay-summary-csv
        path: delayed_summary_*.csv

```

## output

![image](https://github.com/user-attachments/assets/4bc40c88-5f76-458a-9b26-c959960899cf)
