import pandas as pd

df = pd.read_csv('transactions.csv')

# print(df.head())
# print(df.info())

df['amount'] = df['amount'].astype(float)

df['transaction_day'] = pd.to_datetime(df['transaction_day'],errors='coerce')
df['timestamp'] = pd.to_datetime(df['timestamp'])
print(df.head())
print(df.info())

usd_high_value = df[(df['currency']=='USD') & (df['amount'] > 10000)]

print(usd_high_value[['currency','timestamp','amount']].head())