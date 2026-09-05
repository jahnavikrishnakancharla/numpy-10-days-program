# Day 02 - NumPy Indexing and Slicing
# 10-Day NumPy Learning Journey
# Goal: Learn indexing, slicing, and modifying NumPy arrays

import numpy as np

# --------------------------------------------------
# 1. 1D Array Indexing
# --------------------------------------------------

arr = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(arr)

print("\n1D Indexing:")
print("First element:", arr[0])
print("Third element:", arr[2])
print("Last element:", arr[-1])
print("Second last element:", arr[-2])


# --------------------------------------------------
# 2. 1D Array Slicing
# --------------------------------------------------

print("\n1D Slicing:")
print("Elements from index 1 to 3:", arr[1:4])
print("First 3 elements:", arr[:3])
print("From index 2:", arr[2:])
print("Every second element:", arr[::2])


# --------------------------------------------------
# 3. 2D Array Indexing
# --------------------------------------------------

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Array:")
print(arr2)

print("\n2D Indexing:")
print("Element at row 1, column 1:", arr2[1, 1])
print("Element at row 2, column 0:", arr2[2, 0])
print("Element at row 0, column 2:", arr2[0, 2])


# --------------------------------------------------
# 4. Selecting Rows and Columns
# --------------------------------------------------

print("\nRows and Columns:")
print("Second row:", arr2[1])
print("Second column:", arr2[:, 1])


# --------------------------------------------------
# 5. 2D Array Slicing
# --------------------------------------------------

print("\n2D Slicing:")
print("First two rows and columns:")
print(arr2[0:2, 0:2])

print("\nLast two rows and columns:")
print(arr2[1:, 1:])


# --------------------------------------------------
# 6. Modifying Array Values
# --------------------------------------------------

arr3 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

arr3[1, 1] = 500

print("\nModified Array:")
print(arr3)


# --------------------------------------------------
# 7. Data Analysis Practice
# --------------------------------------------------

marks = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80]
])

print("\nStudent Marks:")
print(marks)

print("\nPython marks of all students:")
print(marks[:, 0])

print("\nSQL marks of all students:")
print(marks[:, 1])

print("\nMarks of second student:")
print(marks[1])

print("\nExcel mark of third student:")
print(marks[2, 2])


# --------------------------------------------------
# Day 2 Key Learnings
# --------------------------------------------------

print("\nDay 2 Key Learnings:")
print("- Learned 1D array indexing")
print("- Learned negative indexing")
print("- Learned 1D array slicing")
print("- Learned 2D array indexing")
print("- Learned row and column selection")
print("- Learned 2D array slicing")
print("- Learned how to modify array values")
print("- Practiced extracting data from a marks dataset")
