import numpy as np
a = np.array([10, 20, 30])
b = np.array([40, 50, 60])
result=np.concatenate((a,b))
print(result)

result=np.vstack((a,b))
print(result)

result=np.hstack((a,b))
print(result)

arr = np.array([10, 20, 30, 40, 50, 60])
print(np.split(arr,3))

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])
print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))

jan = np.array([100, 200, 150])
feb = np.array([180, 220, 170])
print(np.concatenate((jan,feb)))
print(np.vstack((jan,feb)))
print(np.hstack((jan,feb)))
