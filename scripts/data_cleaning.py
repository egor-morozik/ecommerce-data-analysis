import pandas as pd

df = pd.read_csv('data/online_retail.csv', encoding='ISO-8859-1')

print("Old data:")
print(df.info())
print("\nSkip data:")
print(df.isnull().sum())

df = df.dropna(subset=['CustomerID'])  
df = df.dropna(subset=['Description'])  

df = df.drop_duplicates()

df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['CustomerID'] = df['CustomerID'].astype(str)

print("\nAfter cleaning:")
print(df.describe())

df.to_csv('data/online_retail_cleaned.csv', index=False)
print("Save data in data/online_retail_cleaned.csv")