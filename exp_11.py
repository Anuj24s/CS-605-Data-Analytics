import pandas as pd
import numpy as np

# Create dictionary data
data = {
    'name': ['Dinesh', 'Suresh', 'Rahul', 'Ravi', 'Manoj',
             'Hari', 'Yatharth', 'Saurabh', 'Kapil', 'Salini'],
    'runs': [125, 129, 165, np.nan, 109, 120, 145, np.nan, 118, 119],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
}

# Index labels
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Create DataFrame
df = pd.DataFrame(data, index=labels)

# Display first 3 rows
print(df.head(3))