import numpy as np 

arr =np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr=arr.reshape(2,2,-1) #-1 its Unknown Dimension suitable dimension select

print(arr.shape)
print(newarr.shape)

print (newarr)
