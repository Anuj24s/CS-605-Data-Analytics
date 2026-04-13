import pandas as pd
import numpy as np

# Create dataset
data = {
    'Price': [13500, 13750, 13950, 14950, 15500],
    'FuelType': ['Diesel', np.nan, 'Petrol', np.nan, 'CNG'],
    'KM': [46986, 72937, 41711, 48000, 38500]
}

# Create DataFrame
df = pd.DataFrame(data)

# Select rows where FuelType is NaN
missing_fuel = df[df['FuelType'].isnull()]

# Display result
print(missing_fuel)