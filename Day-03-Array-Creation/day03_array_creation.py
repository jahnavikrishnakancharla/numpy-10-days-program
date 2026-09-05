# Day 03 - NumPy Array Creation
# 10-Day NumPy Learning Journey
# Goal: Learn different methods to create NumPy arrays

import numpy as np

# Creating an array of zeros
arr = np.zeros(5)
print(arr)

# Creating a 3x3 array of ones
arr = np.ones((3, 3))
print(arr)

# Creating a 2x4 array filled with 25
arr = np.full((2, 4), 25)
print(arr)

# Creating numbers from 10 to 20
arr = np.arange(10, 21)
print(arr)

# Creating even numbers from 2 to 10
arr = np.arange(2, 11, 2)
print(arr)

# Creating 6 evenly spaced values from 0 to 10
arr = np.linspace(0, 10, 6)
print(arr)

# Creating a 4x4 identity matrix
arr = np.eye(4)
print(arr)
