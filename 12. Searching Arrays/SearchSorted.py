import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr,7) # if not found return last index+1 that means all index are serching but not found.Right now, index position is last index+1

print(x)