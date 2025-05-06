import numpy as np 

arr =np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr=arr.reshape(2,3,2)

print(arr.shape)
print(newarr.shape)

print (newarr)


print(arr.reshape(2,3,2).base) #that means reshape return to view 