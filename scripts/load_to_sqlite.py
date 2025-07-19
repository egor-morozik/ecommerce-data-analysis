import pandas as pd
import sqlite3

df = pd.read_csv('data/online_retail_cleaned.csv')

conn = sqlite3.connect('data/ecommerce.db')
df.to_sql('transactions', conn, if_exists='replace', index=False)

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM transactions")
print(f"Records count: {cursor.fetchone()[0]}")
conn.close()