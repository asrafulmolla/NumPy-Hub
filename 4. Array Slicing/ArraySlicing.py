import numpy as np

arr =np.array([1,2,3,4,5,6])

# [start] [end-1] [Step]

print (arr[1:6]) # one to 6-1 index print 

print (arr[:6]) # first to 6-1 index print 

print (arr[1:]) #one index to last peint 

print (arr[0:len(arr)]) # first to last print 

print (arr[0:len(arr):2]) # 0 to last 2 increment print 

print (arr[::-1]) # reverse array 

print(arr[-3:-1])