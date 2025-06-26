### Importing packages
```
import pandas as pd
import numpy as np
```
#### Load the order data
```
df = pd.read_csv('orders.csv')
```

#### Standardize column names to lowercase without spaces
```

df.columns = df.columns.str.strip().str.lower()
```


#### Convert date columns to datetime with error coercion
```

date_cols = ['order_date', 'delivery_date', 'submitted_at']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
```

#### Fill missing delivery dates with today's date
```

if 'delivery_date' in df.columns:
    df['delivery_date'] = df['delivery_date'].fillna(pd.Timestamp.today())
```

#### Calculate delay days as delivery_date - order_date
```
if 'order_date' in df.columns and 'delivery_date' in df.columns:
    df['delay_days'] = (df['delivery_date'] - df['order_date']).dt.days
else:
    # Fallback if order_date missing: use today - delivery_date
    df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
```

#### Flag delayed orders (threshold: delay > 3 days)
```

df['delayed'] = np.where(df['delay_days'] > 3, 1, 0)
```

#### Aggregate delayed counts per customer
```

top_delayed = df.groupby('customer_id')['delayed'].sum().sort_values(ascending=False)

print("\nTop 5 Delayed Customers:")
print(top_delayed.head(5))
```

#### Analyze feedback text if available
```
if 'feedback' in df.columns:
    issues = (
        df['feedback']
        .dropna()
        .str.lower()
        .str.extractall(r'(\b\w+\b)')[0]
        .value_counts()
        .head(10)
    )
    print("\nMost Common Words in Feedback Issues:")
    print(issues)
else:
    print("\nNo 'feedback' column found for issue analysis.")
```

#### Save the processed dataset to CSV
```
df.to_csv('preprocessed_customer_orders.csv', index=False)
```
