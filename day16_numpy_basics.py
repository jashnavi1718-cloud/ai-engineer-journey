# Day 16: NumPy Basics

import numpy as np

# Create NumPy array
arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("Array type:", type(arr))

# Basic operations
print("Add 2:", arr + 2)
print("Multiply by 2:", arr * 2)

print("--------------------")

# 2D Array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("2D Array:")
print(matrix)

print("Shape:", matrix.shape)
print("Size:", matrix.size)
