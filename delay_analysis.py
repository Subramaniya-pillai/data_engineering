import pandas as pd
from datetime import datetime

# Load data
df = pd.read_csv('supply_chain_orders.csv')

# Convert to datetime
df['delivery_date'] = pd.to_datetime(df['delivery_date'])

# Calculate delay
df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
df['is_delayed'] = (df['delay_days'] > 0).astype(int)

# Summary
summary = df[df['is_delayed'] == 1].groupby('supplier_id')['order_id'].count().reset_index()
summary.columns = ['supplier_id', 'delayed_orders']

# Save output
output_file = f'delayed_summary_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
summary.to_csv(output_file, index=False)

print(" Delay summary saved to:", output_file)
