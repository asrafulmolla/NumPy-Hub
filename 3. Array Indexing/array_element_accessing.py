# 1D array accesig 
import numpy as np 

arr = np.array([1,2,3,4,5,6])

print (arr[2])

# 2d array accesing

arr2=np.array([[1,2,3,4],[5,6,7,8]])

print (arr2[1,1]) #row col

# 3d array accessing

arr3=np.array([[[1,2,3],[4,5,6]],[[9,8,7],[5,4,3]]])
print (arr3[1,1,1]) 

# nagative indexing

arr2=np.array([[1,2,3,4],[5,6,7,8]])

print (arr2[1,-1]) #nagative last theke suru kore   