import pandas as pd
import matplotlib.pyplot as plt

# Create dataset (total price per month)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
    'Total_Price': [2200, 2700, 3100, 2900, 3300, 3600, 3000, 2800]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot histogram
plt.hist(df['Total_Price'], bins=5)

# Labels
plt.xlabel('Price Range')
plt.ylabel('Frequency')
plt.title('Histogram of Total Monthly Prices')

# Show plot
plt.show()