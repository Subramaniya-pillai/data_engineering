#  Week 4 – ETL on Supply Chain Data using Databricks

##  Objective
Build an ETL pipeline to clean and transform supply chain order data in **Databricks Community Edition** using PySpark, and save the processed output for further analytics.

---

##  Input File
`supply_chain_orders.csv` (Sample Format):

| order_id | supplier_id | delivery_date |
|----------|-------------|----------------|
| O101     | S010        | 2024-06-01     |
| O102     | S011        | 2024-06-10     |

>  **File Location:**  
`/Volumes/workspace/default/subramani/supply_chain_orders.csv`

---

##  ETL Steps Performed

### 1.  Load CSV File
Load the supply chain orders into a PySpark DataFrame using `spark.read.csv()`.

### 2.  Convert Delivery Date
Convert `delivery_date` column from string to date format using `to_date()`.

### 3. ⏱ Calculate Delay Days
Add a new column `delay_days` by subtracting `delivery_date` from the current date.

### 4.  Flag Delays
Create a new column `is_delayed` which flags shipments delayed (`delay_days > 0`) as `1`, otherwise `0`.

### 5.  Save Transformed Output
Save the cleaned and transformed DataFrame 

---

## Code:

```
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, current_date, datediff, col, when

# Step 1: Start Spark session
spark = SparkSession.builder.appName("Week4_ETL_SupplyChain").getOrCreate()

# Step 2: Load input CSV file
input_path = "/Volumes/workspace/default/subramani/supply_chain_orders.csv"
df = spark.read.option("header", True).csv(input_path)


print("🔹 Step 2: Raw Data")
df.show(5, truncate=False)  # Safely preview only top 5 rows


# Step 3: Convert 'delivery_date' to DateType
df = df.withColumn("delivery_date", to_date(col("delivery_date"), "yyyy-MM-dd"))

print("🔹 Step 3: After converting 'delivery_date' to date")
df.show()

# Step 4: Calculate 'delay_days' as the difference from today
df = df.withColumn("delay_days", datediff(current_date(), col("delivery_date")))

print("🔹 Step 4: After calculating 'delay_days'")
df.show()

# Step 5: Add 'is_delayed' column (1 if delay_days > 0, else 0)
df = df.withColumn("is_delayed", when(col("delay_days") > 0, 1).otherwise(0))

print("🔹 Step 5: After adding 'is_delayed' column")
df.show()

# Step 6: Save to CSV (overwrite previous version)
output_path = "/Volumes/workspace/default/subramani/week4_etl_output_csv"
df.coalesce(1).write.mode("overwrite").option("header", True).csv(output_path)

print(f" Step 6: Data saved to {output_path}")

# Step 7: Create temporary view and run SQL to get top 5 delayed
df.createOrReplaceTempView("supply_orders")

result = spark.sql("""
  SELECT order_id, supplier_id, delay_days
  FROM supply_orders
  WHERE is_delayed = 1
  ORDER BY delay_days DESC
  LIMIT 5
""")

print("🔹 Step 7: Top 5 delayed orders")
result.show()

# Step 8: Stop Spark session
spark.stop()

```

