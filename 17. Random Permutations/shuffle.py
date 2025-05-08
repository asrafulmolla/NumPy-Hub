import numpy as np 
from numpy import random

arr =np.array([1,2,3,4,5,6]) #The shuffle() method makes changes to the original array.

random.shuffle(arr)

print (arr)