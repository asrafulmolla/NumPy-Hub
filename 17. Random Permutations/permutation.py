import numpy as np 
from numpy import random

arr =np.array([1,2,3,4,5,6]) # The permutation() method returns a re-arranged array (and leaves the original array un-changed).

newarr=random.permutation(arr)

print (newarr)