import numpy as np 

arr =np.array([1,2,3,4,5])

a=arr.view()
a[0]=100  # ekta cng hole auto 2tai cng hoye jabe
arr[2]=55  # ekta cng hole auto 2tai cng hoye jabe

print (arr)
print (a)