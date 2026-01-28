# Day 17: NumPy Advanced Operations

import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

# Indexing
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("First three elements:", arr[:3])
print("Middle elements:", arr[1:4])

print("--------------------")

# Mathematical functions
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

print("--------------------")

# 2D Array operations
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("2D Array:")
print(matrix)

print("Column-wise sum:", np.sum(matrix, axis=0))
print("Row-wise sum:", np.sum(matrix, axis=1))
