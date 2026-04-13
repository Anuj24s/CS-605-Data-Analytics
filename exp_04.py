import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Petrol': [120, 150, 170, 160, 180, 200],
    'CNG': [80, 90, 100, 110, 120, 130]
}

# Create DataFrame
df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# -------- Heatmap --------
plt.figure(figsize=(6,4))
plt.imshow(df, cmap='viridis', aspect='auto')

plt.colorbar(label='Sales')
plt.xticks(ticks=[0,1], labels=df.columns)
plt.yticks(ticks=range(len(df.index)), labels=df.index)

plt.title('Heatmap of Petrol and CNG Sales')
plt.xlabel('Fuel Type')
plt.ylabel('Month')

plt.show()

# -------- Bar Chart --------
months = df.index
x = np.arange(len(months))

plt.figure(figsize=(6,4))
plt.bar(x - 0.2, df['Petrol'], width=0.4, label='Petrol')
plt.bar(x + 0.2, df['CNG'], width=0.4, label='CNG')

plt.xticks(x, months)
plt.xlabel('Months')
plt.ylabel('Units Sold')
plt.title('Monthly Sales Comparison')

plt.legend()

plt.show()