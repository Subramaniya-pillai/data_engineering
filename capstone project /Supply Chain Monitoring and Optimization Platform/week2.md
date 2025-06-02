#  <p align="center">Week 2 – Data Collection & Preprocessing in Python </p>

### Objective:

Build a robust data preprocessing pipeline to ingest supply chain data from structured files (CSV/JSON), clean it using pandas, and compute useful metrics like delivery delays and total cost using NumPy, preparing the data for analytics and further processing.

### Data Source
Created a custom CSV file orders.csv containing supply chain data such as orders, suppliers, delivery dates, and product info.

### Steps Performed

### Step 1: Load CSV

```
df = pd.read_csv("orders.csv")
```
###  Step 2: Clean and format dates

```
df.dropna(subset=['order_id', 'supplier_id', 'delivery_date', 'order_date'], inplace=True)
df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

```
### Step 3: Calculate delay


```
df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
df['is_delayed'] = np.where(df['delay_days'] > 0, 1, 0)

```

### Step 4: Calculate total cost
```
df['total_cost'] = df['quantity'] * df['unit_price']
```
### Step 5: Optional filtering (e.g., only delayed or pending orders)
```
delayed_orders = df[df['is_delayed'] == 1]
pending_orders = df[df['status'].str.lower() == 'pending']
```
### Step 6: Output cleaned and processed data
```
print("\n All Processed Orders:")
print(df[['order_id', 'product_name', 'quantity', 'order_date', 'delivery_date', 'delay_days', 'is_delayed', 'total_cost']])
```
### Optional: Export processed data
```
df.to_csv("processed_orders_output.csv", index=False)
```
Output:
Displayed the processed DataFrame and saved the cleaned data back to a CSV file for future use.


![image](https://github.com/user-attachments/assets/a1748cad-d8eb-4993-bc08-6acb5ce665a5)


