from numpy import random

num = random.randint(100) # random number generator 1 to 100
print (num)

num1=random.randint(100, size=(5))
print (num1)

num2=random.randint(100, size=(3,5))
print (num2)