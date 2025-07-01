import pandas as pd
import numpy as np

df = pd.read_csv('orders.csv')
df['delivery_date'] = pd.to_datetime(df['delivery_date'])
df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
df['delayed'] = np.where(df['delay_days'] > 0, 1, 0)

summary = df.groupby('customer_id')['delayed'].sum().sort_values(ascending=False)
summary.to_csv('delay_summary.csv', header=True)
print(" Delay summary generated.")
