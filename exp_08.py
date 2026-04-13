import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Petrol': [120, 150, 170, 160, 180, 200],
    'Diesel': [100, 130, 140, 150, 160, 170],
    'CNG': [80, 90, 100, 110, 120, 130]
}

# Create DataFrame
df = pd.DataFrame(data)

# Stack plot
plt.stackplot(
    df['Month'],
    df['Petrol'],
    df['Diesel'],
    df['CNG'],
    labels=['Petrol', 'Diesel', 'CNG']
)

# Labels and legend
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Fuel Sales Stack Plot')
plt.legend()

# Show plot
plt.show()