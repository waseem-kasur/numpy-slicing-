import numpy as np 
arr=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr[2,2])
print(arr[3,3])
############ Column Row  ########################
print(arr[0:3,0:3])
print(arr[1:,1:])
print(arr[1:3,1:3])
