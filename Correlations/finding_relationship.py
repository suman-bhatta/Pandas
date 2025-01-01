import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('data.csv')

# Print the first few rows to inspect the data
print("DataFrame Head:")
print(df.head())

# Print the data types of each column to identify non-numeric columns
print("\nData Types:")
print(df.dtypes)

# Strip any whitespace from column names
df.columns = df.columns.str.strip()

# Convert all columns to numeric where possible, coerce errors to NaN
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with NaN values in any column (optional)
df = df.dropna()

# Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Compute and print the correlation matrix
print("\nCorrelation Matrix:")
print(numeric_df.corr())
