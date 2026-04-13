import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (you can replace with your dataset)
data = {
    'Fuel_Type': ['Petrol', 'Diesel', 'Petrol', 'CNG', 'Diesel', 'CNG'],
    'Price': [1000, 1500, 1200, 800, 1300, 900]
}

df = pd.DataFrame(data)

# Calculate total price for each Fuel Type
total_price = df.groupby('Fuel_Type')['Price'].sum()

# Plot the line graph
plt.plot(total_price.index, total_price.values, linestyle='dotted', color='red', 
        marker='o', markerfacecolor='red',linewidth=3, label='Total Price')

# Labels and legend
plt.xlabel('Fuel Type')
plt.ylabel('Price')
plt.legend(loc='upper right')

# Show plot
plt.show()