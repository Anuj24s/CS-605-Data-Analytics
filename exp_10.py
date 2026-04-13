import pandas as pd

# Read CSV file
df = pd.read_csv('Toyota.csv')

# Display first few rows
print("First 5 Rows:\n")
print(df.head())

# Display basic information
print("\nDataFrame Info:\n")
df.info()

# Display index and columns
print("\nIndex:", df.index)
print("\nColumns:", df.columns)

# Display number of null values in each column
print("\nNull Values in Each Column:\n")
print(df.isnull().sum())

# Display basic statistics
print("\nStatistical Summary:\n")
print(df.describe())