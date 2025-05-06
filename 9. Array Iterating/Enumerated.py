import numpy as np 

arr =np.array([1,2,3,4,5,6,7,8])

for idx, x in np.ndenumerate(arr):
    print (idx, x)
    
    
arr2 =np.array([[1,2,3,4],[5,6,7,8]])

for idx, x in np.ndenumerate(arr2):
    print (idx, x)
    
    
arr3 =np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for idx, x in np.ndenumerate(arr3):
    print (idx, x)