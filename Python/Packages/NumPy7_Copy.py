import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,0],[9,8,7,6,5]])
arr1=arr.view()
arr1[1,0:2]=34
arr[0,2]=34
print(arr1)
print(arr)
