import numpy as np 

arr0=np.array(23)
arr2 =np.array([[1,2,3,4,5], [6,7,8,9,1]])
arr3 =np.array([[[1,2,3,4,5], [6,7,8,9,1]],[[1,2,3,4,5],[2,3,4,5,6]]])
arr5 =np.array([1,2,3,4,5], ndmin=8)

print(arr0.shape)
print (arr2.shape)
print (arr3.shape)
print (arr5.shape)