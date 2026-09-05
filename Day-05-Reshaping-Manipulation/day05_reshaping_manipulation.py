# Day 05 - NumPy Reshaping and Array Manipulation
# 10-Day NumPy Learning Journey
# Goal: Learn reshape, flatten, ravel, and transpose

import numpy as np

# 1. Reshape 1D array into 2 rows and 3 columns
arr = np.array([1, 2, 3, 4, 5, 6])

arr1 = arr.reshape(2, 3)
print("2 x 3 Array:")
print(arr1)


# 2. Reshape into 3 rows and 2 columns
arr2 = arr.reshape(3, 2)
print("\n3 x 2 Array:")
print(arr2)


# 3. Convert 2D array into 1D using flatten()
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nFlatten:")
print(arr.flatten())


# 4. Convert 2D array into 1D using ravel()
print("\nRavel:")
print(arr.ravel())


# 5. Transpose the array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nTranspose:")
print(arr.T)


# Day 5 Key Learnings
print("\nDay 5 Key Learnings:")
print("- Learned reshape()")
print("- Learned flatten()")
print("- Learned ravel()")
print("- Learned transpose using .T")
