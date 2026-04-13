import pandas as pd
import matplotlib.pyplot as plt

# Create dataset (monthly price for each fuel type)
data = {
    'Fuel_Type': ['Petrol', 'Diesel', 'CNG'],
    'Jan': [1000, 1200, 800],
    'Feb': [1100, 1300, 850],
    'Mar': [1200, 1400, 900],
    'Apr': [1300, 1500, 950],
    'May': [1400, 1600, 1000],
    'Jun': [1500, 1700, 1050]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total yearly price for each Fuel Type
df['Total'] = df.iloc[:, 1:].sum(axis=1)

# Pie chart
plt.pie(
    df['Total'],
    labels=df['Fuel_Type'],
    autopct='%1.1f%%'
)

# Title
plt.title('Total Yearly Price by Fuel Type')

# Show plot
plt.show()
