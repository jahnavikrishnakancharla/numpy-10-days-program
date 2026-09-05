# Day 07 - NumPy Broadcasting and Vectorization
# 10-Day NumPy Learning Journey
# Goal: Learn vectorization and broadcasting

import numpy as np

# 1. Vectorization
arr = np.array([10, 20, 30, 40, 50])

print("Add 10:")
print(arr + 10)

print("Subtract 5:")
print(arr - 5)

print("Multiply by 2:")
print(arr * 2)

print("Divide by 5:")
print(arr / 5)


# 2. Broadcasting - Add 5 to every mark
marks = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [95, 88, 92]
])

print("\nMarks + 5:")
print(marks + 5)


# 3. Column-wise Broadcasting
bonus1 = np.array([5, 2, 3])

print("\nColumn-wise Bonus:")
print(marks + bonus1)


# 4. Student-wise Broadcasting
bonus = np.array([
    [5],
    [10],
    [2]
])

print("\nStudent-wise Bonus:")
print(marks + bonus)


# 5. Vectorized Comparisons
marks = np.array([45, 67, 82, 90, 55])

print("\nMarks greater than 60:")
print(marks > 60)

print("\nMarks greater than or equal to 50:")
print(marks >= 50)

print("\nMarks less than 70:")
print(marks < 70)


# 6. Data Analyst Challenge - Salary
salary = np.array([
    [30000, 35000, 40000],
    [45000, 50000, 55000],
    [60000, 65000, 70000]
])

# Add 5000 to everyone
print("\nSalary + 5000:")
print(salary + 5000)

# Different increments for each column
bonus = np.array([3000, 5000, 7000])

print("\nColumn-wise Salary Increment:")
print(salary + bonus)


# Day 7 Key Learnings
print("\nDay 7 Key Learnings:")
print("- Learned vectorization")
print("- Learned broadcasting")
print("- Learned scalar broadcasting")
print("- Learned row/column broadcasting")
print("- Learned vectorized comparisons")
print("- Practiced salary calculations without loops")
