import pandas as pd 

# DataFrame examples
df1 = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
df2 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
df3 = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])

# Series examples
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# Print the results
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
print("\nDataFrame 3:")
print(df3)

print("\nSeries 1:")
print(series1)
print("\nSeries 2:")
print(series2)
