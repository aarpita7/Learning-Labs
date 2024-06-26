# Introduction to Pandas
# Pandas is an open-source data analysis and manipulation library for Python.
# It provides data structures and functions needed to manipulate structured data seamlessly.


# Importing Pandas
import pandas as pd

# Pandas Series
# A Pandas Series is a one-dimensional array-like object that can hold any data type such as integers, floats, strings, etc.
# Each element in a Series has a unique label, also called an index.

# Creating a Pandas Series
# Let's create a simple Pandas Series from a list
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("Pandas Series from a list:")
print(series)

# Creating a Pandas Series with custom index
data = [1, 2, 3, 4, 5]
index = ['a', 'b', 'c', 'd', 'e']
series_with_index = pd.Series(data, index=index)
print("\nPandas Series with custom index:")
print(series_with_index)

# Creating a Pandas Series from a dictionary
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
series_from_dict = pd.Series(data)
print("\nPandas Series from a dictionary:")
print(series_from_dict)

# Accessing data in a Pandas Series
# You can access elements in a Series by their index
print("\nAccessing elements in a Series:")
print("Element at index 'c':", series_with_index['c'])
print("First element:", series_with_index[0])

# Performing operations on a Pandas Series
# You can perform various operations on a Pandas Series, such as arithmetic operations, filtering, etc.
print("\nPerforming operations on a Series:")
print("Series + 10:")
print(series + 10)
print("Series > 3:")
print(series > 3)

# Summary
# - Pandas is a powerful library for data analysis and manipulation in Python.
# - You can install Pandas using pip.
# - A Pandas Series is a one-dimensional array-like object that can hold any data type.
# - You can create a Pandas Series from a list, dictionary, or with a custom index.
# - You can access elements in a Series by their index and perform various operations on the Series.


