import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr+10)
print(arr-5)
print(arr*2)
print(arr/10)

a =np.array([10, 20, 30, 40])
b =np.array([1, 2, 3, 4])
print(a+b)
print(a-b)
print(a*b)

marks = np.array([85, 72, 90, 65, 95, 78])
print(sum(marks))
print(sum(marks)/len(marks))
print(min(marks))
print(max(marks))

print(marks>75)
print(marks < 70)
print(marks == 95)


marks = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80]
])
print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
