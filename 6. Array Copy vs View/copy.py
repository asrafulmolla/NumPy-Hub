import numpy as np 

arr =np.array([1,2,3,4,5])

a=arr.copy()
arr[0]=10

print (arr)
print (a)