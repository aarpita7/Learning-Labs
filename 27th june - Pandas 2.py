
import pandas as pd

# Data Cleaning
# Handling missing data
data = {
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': [9, 10, 11, None]
}
df = pd.DataFrame(data)
print("Original DataFrame with missing values:")
print(df)

# Filling missing values
df_filled = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_filled)

# Dropping rows with missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)

# Merging DataFrames
# Creating two DataFrames to merge
data1 = {
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
}
data2 = {
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merging on 'key' column
merged_df = pd.merge(df1, df2, on='key', how='inner')
print("\nMerged DataFrame (inner join):")
print(merged_df)





