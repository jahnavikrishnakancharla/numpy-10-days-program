# Day 01 - NumPy Basics
# 10-Day NumPy Learning Journey
# Goal: Learn NumPy fundamentals for Data Analysis

# --------------------------------------------------
# 1. Import NumPy
# --------------------------------------------------

import numpy as np


# --------------------------------------------------
# 2. Creating a 1D NumPy Array
# --------------------------------------------------

arr = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(arr)


# --------------------------------------------------
# 3. Creating a 2D NumPy Array
# --------------------------------------------------

arr1 = np.array([
    [1, 4, 3, 7],
    [8, 9, 6, 2]
])

print("\n2D Array:")
print(arr1)


# --------------------------------------------------
# 4. Number of Dimensions - ndim
# --------------------------------------------------

print("\nNumber of dimensions:")
print("arr:", arr.ndim)
print("arr1:", arr1.ndim)


# --------------------------------------------------
# 5. Shape of Array
# --------------------------------------------------

print("\nShape of arrays:")
print("arr:", arr.shape)
print("arr1:", arr1.shape)


# --------------------------------------------------
# 6. Number of Elements - size
# --------------------------------------------------

print("\nNumber of elements:")
print("arr:", arr.size)
print("arr1:", arr1.size)


# --------------------------------------------------
# 7. Data Type - dtype
# --------------------------------------------------

print("\nData types:")
print("arr:", arr.dtype)
print("arr1:", arr1.dtype)


# --------------------------------------------------
# 8. Basic Indexing in a 2D Array
# --------------------------------------------------

arr2 = np.array([
    [10, 80, 30],
    [40, 50, 60]
])

print("\nBasic Indexing:")

# Access 50
print("Element at [1, 1]:", arr2[1, 1])

# Access 80
print("Element at [0, 1]:", arr2[0, 1])

# Access 30
print("Element at [0, 2]:", arr2[0, 2])


# --------------------------------------------------
# 9. Day 1 Key Learnings
# --------------------------------------------------

print("\nDay 1 Key Learnings:")
print("- Learned how to import NumPy")
print("- Learned how to create 1D and 2D arrays")
print("- Learned ndim")
print("- Learned shape")
print("- Learned size")
print("- Learned dtype")
print("- Learned basic array indexing")
