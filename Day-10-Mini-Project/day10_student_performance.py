# Day 10 - NumPy Mini Project
# Student Performance Analysis
# 10-Day NumPy Learning Journey
# Goal: Apply NumPy concepts to a real-world data analysis problem

import numpy as np


# Student marks
# Columns: Python, SQL, Excel
students = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80],
    [65, 72, 68],
    [90, 95, 92]
])

print("Student Marks:")
print(students)


# 1. Basic Dataset Information
print("\nDataset Shape:")
print(students.shape)

print("\nNumber of Students:")
print(students.shape[0])

print("\nNumber of Subjects:")
print(students.shape[1])

print("\nTotal Number of Marks:")
print(students.size)


# 2. Subject-wise Average
print("\nSubject-wise Average:")
print("Python:", np.mean(students[:, 0]))
print("SQL:", np.mean(students[:, 1]))
print("Excel:", np.mean(students[:, 2]))


# 3. Highest and Lowest Mark
print("\nHighest Mark:")
print(np.max(students))

print("\nLowest Mark:")
print(np.min(students))


# 4. Overall Average of Each Student
student_average = np.mean(students, axis=1)

print("\nStudent Averages:")
print(student_average)


# 5. Students with Average Above 80
print("\nStudent Averages Above 80:")
print(student_average[student_average > 80])


# 6. Pass / Fail Classification
result = np.where(student_average >= 50, "Pass", "Fail")

print("\nPass / Fail:")
print(result)


# 7. Best Student Average
best_student = np.max(student_average)

print("\nBest Student Average:")
print(best_student)


# 8. Median of All Marks
print("\nMedian of All Marks:")
print(np.median(students))


# 9. Standard Deviation
print("\nStandard Deviation:")
print(np.std(students))


# 10. Sort Each Student's Marks
print("\nSorted Marks:")
print(np.sort(students, axis=1))


# 11. Python Marks Greater Than 80
python_marks_above_80 = students[students[:, 0] > 80]

print("\nStudents with Python Marks Above 80:")
print(python_marks_above_80)


# 12. Add 10 Bonus Marks to Python
bonus_python_marks = students[:, 0] + 10

print("\nPython Marks After 10-Mark Bonus:")
print(bonus_python_marks)


# Final Learning Summary
print("\nDay 10 Key Learnings:")
print("- Applied NumPy to a real-world dataset")
print("- Used indexing and slicing")
print("- Used statistical functions")
print("- Used Boolean masking")
print("- Used np.where()")
print("- Used sorting")
print("- Used broadcasting")
print("- Performed student performance analysis")
