from numpy import random

x=random.choice([2,3,4,5])
print (x)


xx=random.choice([2,3,4,5], size=(5))
print (xx)

xxx=random.choice([2,3,4,5], size=(5,3))
print (xxx)