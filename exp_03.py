import pandas as pd
import matplotlib.pyplot as plt

# Create dataset (monthly Petrol sales)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Petrol': [120, 150, 170, 160, 180, 200]
}

# Create DataFrame
df = pd.DataFrame(data)

# Scatter plot
plt.scatter(df['Month'], df['Petrol'], color='blue', label='Petrol Sales')

# Labels
plt.xlabel('Months')
plt.ylabel('Petrol Sales')

# Add grid with "--" style
plt.grid(linestyle='--')

# Legend
plt.legend()

# Show plot
plt.show()