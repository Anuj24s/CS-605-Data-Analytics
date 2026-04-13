import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Petrol': [120, 150, 170, 160, 180, 200],
    'Diesel': [100, 130, 140, 150, 160, 170]
}

# Create DataFrame
df = pd.DataFrame(data)

# Subplot 1 (Petrol)
plt.subplot(1, 2, 1)
plt.plot(df['Month'], df['Petrol'], marker='o')
plt.title('Petrol Sales')
plt.xlabel('Month')
plt.ylabel('Sales')

# Subplot 2 (Diesel)
plt.subplot(1, 2, 2)
plt.plot(df['Month'], df['Diesel'], marker='o')
plt.title('Diesel Sales')
plt.xlabel('Month')
plt.ylabel('Sales')

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()