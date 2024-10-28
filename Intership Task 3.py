import matplotlib.pyplot as plt
import pandas as pd
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 10, 37],
    'Trend': [20, 40, 15, 35]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 5))
plt.bar(df['Category'], df['Values'], color='blue', label='Values')
plt.title('Bar Chart of Values by Category')
plt.xlabel('Category')
plt.ylabel('Values')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df['Category'], df['Trend'], marker='o', color='red', label='Trend')
plt.title('Line Chart of Trend by Category')
plt.xlabel('Category')
plt.ylabel('Trend')
plt.legend()
plt.show()
