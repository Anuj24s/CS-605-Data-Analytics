import pandas as pd
import matplotlib.pyplot as plt

# Creating dataset with monthly fuel sales
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Petrol': [120, 150, 170, 160, 180, 200],
    'Diesel': [100, 130, 140, 150, 160, 170],
    'CNG': [80, 90, 100, 110, 120, 130]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set Month column as index
df.set_index('Month', inplace=True)

# Plot multiline graph (separate line for each Fuel Type)
plt.plot(df.index, df['Petrol'], marker='o', label='Petrol')
plt.plot(df.index, df['Diesel'], marker='o', label='Diesel')
plt.plot(df.index, df['CNG'], marker='o', label='CNG')

# Add labels and legend
plt.xlabel('Months')
plt.ylabel("Fuel Sold")
plt.title("Fuel Sales Per Month")
plt.legend()

# Display plot
plt.show()