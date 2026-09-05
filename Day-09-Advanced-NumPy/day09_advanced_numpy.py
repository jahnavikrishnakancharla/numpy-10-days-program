# Day 09 - Advanced NumPy
# 10-Day NumPy Learning Journey
# Goal: Learn Boolean Masking, np.where(), Sorting, Unique Values and Random Numbers

import numpy as np


# 1. Boolean Masking
# Filter values based on a condition
marks = np.array([45, 78, 90, 56, 88, 32, 95, 67])

print("Marks greater than 70:")
print(marks[marks > 70])


# 2. np.where()
# Classify students as Pass or Fail
result = np.where(marks >= 50, "Pass", "Fail")

print("\nPass / Fail:")
print(result)


# 3. Sorting
# Sort marks in ascending order
print("\nSorted Marks:")
print(np.sort(marks))


# 4. Unique Values
# Remove duplicate values
departments = np.array([
    "HR",
    "IT",
    "Sales",
    "IT",
    "HR",
    "Finance"
])

print("\nUnique Departments:")
print(np.unique(departments))


# 5. Random Numbers
# Generate 5 random numbers between 1 and 100
random_marks = np.random.randint(1, 101, 5)

print("\nRandom Marks:")
print(random_marks)


# Day 9 Key Learnings
print("\nDay 9 Key Learnings:")
print("- Learned Boolean Masking")
print("- Learned np.where()")
print("- Learned np.sort()")
print("- Learned np.unique()")
print("- Learned random number generation")
print("- Practiced advanced data filtering and manipulation")


practece


import numpy as np
sales = np.array([1000, 2500, 1800, 4000, 3200, 900])

print(sales[sales > 2000])

salary = np.array([20000, 35000, 50000, 15000, 45000])

result = np.where(salary >= 30000, "High", "Low")

print(result)

prices = np.array([500, 200, 800, 300, 100])

print(np.sort(prices))


departments = np.array([
    "HR",
    "IT",
    "Sales",
    "IT",
    "HR",
    "Finance"
])

print(np.unique(departments))

numbers = np.random.randint(1, 51, 10)

print(numbers)

marks = np.array([45, 78, 90, 56, 88, 32, 95, 67])
print(marks>70)
result=np.where(marks>50,"pass","fail")
print(result)

print(np.sort(marks))
result=np.random.randint(1,100,5)
print(result)

