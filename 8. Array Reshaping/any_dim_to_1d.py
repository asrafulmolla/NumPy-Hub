import numpy as np 

arr =np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

newarr=arr.reshape(-1) #-1 convert to any dimension to 1d 

print(arr.shape)
print(newarr.shape)

print (newarr)
