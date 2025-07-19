import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/online_retail_cleaned.csv')

print("Quantity statistic:")
print(df['Quantity'].describe())

sns.set_style("whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(data=df[df['Quantity'] <= 100], x='Quantity', bins=50)
plt.title('Quantity distribuition (under 100)')
plt.xlabel('Product quantity')
plt.ylabel('Frequency')
plt.savefig('visualizations/quantity_distribution_improved.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.histplot(data=df[df['Quantity'] > 0], x='Quantity', bins=50, log_scale=True)
plt.title('Quantity  distribuition (log_scale)')
plt.xlabel('Product quantity (log)')
plt.ylabel('Frequency (log)')
plt.savefig('visualizations/quantity_distribution_log.png')
plt.close()
