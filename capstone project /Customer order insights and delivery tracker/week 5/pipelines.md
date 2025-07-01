#  Week 5 – Delay Analysis with GitHub Actions

##  Objective
Automate customer delivery delay analysis using Python and GitHub Actions.

---

##  Folder Structure

data_engineering/

├── order.csv # Raw input data

├── delay_analysis.py # Python script to compute delay summary

├── delay_summary.csv # Generated output (artifact)

└── .github/

└── workflows/

└── python-analysis.yml # CI pipeline for automation



---

## 🛠️ Tools Used
- **Python 3.10**
- **pandas & numpy**
- **GitHub Actions** for CI/CD

---

### Script – `delay_analysis.py`

This script:

- Loads order data from `order.csv`
- Parses delivery dates
- Computes number of delayed days
- Flags delayed deliveries
- Groups by customer ID and summarizes delay counts
- Exports result to `delay_summary.csv`

```python
import pandas as pd
import numpy as np

df = pd.read_csv('order.csv')
df['delivery_date'] = pd.to_datetime(df['delivery_date'])
df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
df['delayed'] = np.where(df['delay_days'] > 0, 1, 0)

summary = df.groupby('customer_id')['delayed'].sum().sort_values(ascending=False)
summary.to_csv('delay_summary.csv', header=True)

print(" Delay summary generated.")

```

###  Output

After every push:

The script runs automatically

A delay_summary.csv file is generated

It appears as a downloadable artifact under the GitHub Actions tab


![image](https://github.com/user-attachments/assets/d9b1bb38-7330-44b3-8d39-817e462c68bb)

