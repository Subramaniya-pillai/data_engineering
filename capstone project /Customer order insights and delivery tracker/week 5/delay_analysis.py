import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv('orders.csv')

# Convert delivery date
df['delivery_date'] = pd.to_datetime(df['delivery_date'])

# Calculate delay
df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
df['delayed'] = np.where(df['delay_days'] > 0, 1, 0)

# Summary by customer
summary = df.groupby('customer_id')['delayed'].sum().sort_values(ascending=False)

# Save to file
summary.to_csv('delay_summary.csv', header=True)
print("✅ Delay summary generated and saved.")
