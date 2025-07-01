#  Week 3 – Supply Chain Delay Analysis with PySpark

##  Objective
Analyze delayed shipments across suppliers using PySpark. This module helps process large supply chain order data, filter delayed orders, and generate summary insights.

---

##  Input File
`supply_chain_orders.csv` (Sample Format):

| order_id | supplier_id | delivery_date |
|----------|-------------|----------------|
| O001     | S001        | 2024-06-01     |
| O002     | S002        | 2024-06-15     |

> File location:  
`/Volumes/workspace/default/subramani/supply_chain_orders.csv`

---

##  Steps Performed

### 1.  Load Data
Read CSV file using PySpark and display the raw records.

### 2.  Convert Date
Convert `delivery_date` column to PySpark DateType using `to_date()`.

### 3.  Calculate Delay
Calculate `delay_days` by comparing `delivery_date` with current date.

### 4.  Filter Delayed Shipments
Filter rows where `delay_days > 0`.

### 5.  Group Summary
Group by `supplier_id` and count delayed shipments.

### 6.  Save Output
Save the summary DataFrame

---

##  PySpark Script: `week3_supplier_delay_summary.py`

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, current_date, datediff, col

# Start Spark session
spark = SparkSession.builder \
    .appName("SupplyChainDelayProcessing") \
    .getOrCreate()

# Step 1: Load CSV data
df = spark.read.option("header", True).csv("/Volumes/workspace/default/subramani/supply_chain_orders.csv")
print("🔹 Raw Data:")
df.show()

# Step 2: Convert delivery_date to proper date format
df = df.withColumn("delivery_date", to_date(col("delivery_date"), "yyyy-MM-dd"))
print("🔹 After converting delivery_date to date:")
df.show()

# Step 3: Calculate delay_days
df = df.withColumn("delay_days", datediff(current_date(), col("delivery_date")))
print("🔹 After calculating delay_days:")
df.show()

# Step 4: Filter delayed shipments (delay_days > 0)
delayed_df = df.filter(col("delay_days") > 0)
print("🔹 Filtered delayed shipments (delay_days > 0):")
delayed_df.show()

# Step 5: Group by supplier_id and count delayed shipments
summary_df = delayed_df.groupBy("supplier_id") \
    .count() \
    .withColumnRenamed("count", "delayed_shipments")
print("🔹 Grouped delay summary by supplier:")
summary_df.show()

# Step 6: Save result to workspace path (no overwrite of previous files)
output_path = "/Volumes/workspace/default/subramani/output_temp"
summary_df.coalesce(1).write.mode("overwrite").option("header", True).csv(output_path)

print(" Output saved to folder:", output_path)

# Stop Spark session
spark.stop()

```

---

