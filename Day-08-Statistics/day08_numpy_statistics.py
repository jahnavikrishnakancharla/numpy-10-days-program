# Day 08 - NumPy Statistics
# 10-Day NumPy Learning Journey
# Goal: Learn statistical functions used in Data Analysis

import numpy as np


# 1. Mean - Average
marks = np.array([65, 70, 75, 80, 85, 90, 95])

print("Mean:")
print(np.mean(marks))


# 2. Median - Middle Value
print("\nMedian:")
print(np.median(marks))


# 3. Standard Deviation - Measure of Spread
print("\nStandard Deviation:")
print(np.std(marks))


# 4. Variance - Squared Measure of Spread
print("\nVariance:")
print(np.var(marks))


# 5. Percentiles
print("\nPercentiles:")
print("25th Percentile:", np.percentile(marks, 25))
print("50th Percentile:", np.percentile(marks, 50))
print("75th Percentile:", np.percentile(marks, 75))


# 6. Correlation - Study Hours vs Marks
hours = np.array([1, 2, 3, 4, 5])
study_marks = np.array([50, 60, 70, 80, 90])

print("\nCorrelation between Study Hours and Marks:")
print(np.corrcoef(hours, study_marks))


# 7. Real-World Example - Temperature vs Ice-Cream Sales
temperature = np.array([20, 25, 30, 35, 40])
ice_cream_sales = np.array([100, 150, 200, 250, 300])

print("\nCorrelation between Temperature and Ice-Cream Sales:")
print(np.corrcoef(temperature, ice_cream_sales))


# Day 8 Key Learnings
print("\nDay 8 Key Learnings:")
print("- Learned mean")
print("- Learned median")
print("- Learned standard deviation")
print("- Learned variance")
print("- Learned percentiles")
print("- Learned correlation")
print("- Practiced statistical analysis using NumPy")
