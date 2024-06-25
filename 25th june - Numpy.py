"""
NumPy Overview

NumPy is a fundamental package for scientific computing in Python. It provides support for arrays, matrices, and many mathematical functions to operate on these data structures.

Topics Covered:
1. Installation
2. Importing NumPy
3. Creating Arrays
4. Array Indexing and Slicing
5. Array Operations
6. Mathematical Functions
7. Array Manipulation
8. Linear Algebra
9. Random Numbers
"""

# 1. Installation
# NumPy can be installed using the pip package manager.
# Run the following command in your terminal or command prompt to install NumPy:
# pip install numpy

# 2. Importing NumPy
import numpy as np

# 3. Creating Arrays

# Creating a 1D array
# An array is a central data structure of the NumPy library. It is a grid of values, all of the same type, indexed by a tuple of non-negative integers.
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Creating a 2D array
# A 2D array is an array of arrays (a matrix), which can be created using nested lists.
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Creating an array with a range of elements
# The arange() function returns an array with evenly spaced values within a given interval.
array_range = np.arange(0, 10, 2)
print("Array with range:", array_range)

# Creating an array with zeros
# The zeros() function creates an array filled with zeros. The shape of the array is defined by the parameter passed as an argument.
array_zeros = np.zeros((2, 3))
print("Array with zeros:\n", array_zeros)

# Creating an array with ones
# The ones() function creates an array filled with ones. The shape of the array is defined by the parameter passed as an argument.
array_ones = np.ones((3, 2))
print("Array with ones:\n", array_ones)

# Creating an array with random values
# The random.random() function creates an array filled with random values between 0 and 1. The shape of the array is defined by the parameter passed as an argument.
array_random = np.random.random((2, 2))
print("Array with random values:\n", array_random)

# 4. Array Indexing and Slicing

# Accessing elements
# Elements of an array can be accessed using square brackets and indices. NumPy arrays are zero-indexed.
print("Element at index 0 in 1D array:", array_1d[0])
print("Element at row 1, column 2 in 2D array:", array_2d[1, 2])

# Slicing arrays
# Slicing in NumPy arrays is similar to that in lists. We can specify a range of indices to extract a subset of the array.
print("Sliced array (first 3 elements):", array_1d[:3])
print("Sliced 2D array (first row):\n", array_2d[0, :])

# 5. Array Operations

# Element-wise addition
# NumPy allows element-wise operations on arrays. These operations are applied to each element individually.
array_add = array_1d + 2
print("Array after addition:", array_add)

# Element-wise multiplication
# Similarly, we can perform element-wise multiplication.
array_multiply = array_1d * 2
print("Array after multiplication:", array_multiply)

# Dot product of two arrays
# The dot() function performs the dot product of two arrays. For 1D arrays, it is the inner product of vectors; for 2D arrays, it is equivalent to matrix multiplication.
array_dot = np.dot(array_1d, array_1d)
print("Dot product:", array_dot)

# 6. Mathematical Functions

# Trigonometric functions
# NumPy provides various mathematical functions, including trigonometric functions such as sin(), cos(), and tan().
array_sin = np.sin(array_1d)
print("Sine of array elements:", array_sin)

# Exponential and logarithmic functions
# Exponential and logarithmic functions are available in NumPy, such as exp() for the exponential function and log() for the natural logarithm.
array_exp = np.exp(array_1d)
print("Exponential of array elements:", array_exp)

array_log = np.log(array_1d)
print("Natural logarithm of array elements:", array_log)

# 7. Array Manipulation

# Reshaping an array
# The reshape() function is used to change the shape of an array without changing its data.
array_reshaped = array_1d.reshape((5, 1))
print("Reshaped array:\n", array_reshaped)

# Flattening an array
# The flatten() function converts a multi-dimensional array into a 1D array.
array_flattened = array_2d.flatten()
print("Flattened array:", array_flattened)

# Concatenating arrays
# The concatenate() function is used to join two or more arrays along a specified axis.
array_concatenated = np.concatenate((array_1d, array_1d))
print("Concatenated array:", array_concatenated)

# 8. Linear Algebra

# Linear algebra is a branch of mathematics that is widely used in scientific computing. NumPy provides many functions to perform linear algebra operations.

# Creating matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
# The dot() function can also be used for matrix multiplication.
matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix product:\n", matrix_product)

# Transpose of a matrix
# The transpose() function returns the transpose of a matrix.
matrix_transpose = np.transpose(matrix_a)
print("Transpose of matrix:\n", matrix_transpose)

# Inverse of a matrix
# The linalg.inv() function computes the inverse of a matrix.
matrix_inverse = np.linalg.inv(matrix_a)
print("Inverse of matrix:\n", matrix_inverse)

# Eigenvalues and eigenvectors
# The linalg.eig() function computes the eigenvalues and right eigenvectors of a square array.
eigenvalues, eigenvectors = np.linalg.eig(matrix_a)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# 9. Random Numbers

# NumPy provides functions to generate random numbers, which are useful in various applications such as simulations and statistical analysis.

# Generating random numbers from a normal distribution
# The random.normal() function generates random numbers from a normal (Gaussian) distribution.
random_normal = np.random.normal(0, 1, 5)
print("Random numbers from normal distribution:", random_normal)

# Generating random integers
# The random.randint() function generates random integers between a specified range.
random_integers = np.random.randint(0, 10, 5)
print("Random integers:", random_integers)
