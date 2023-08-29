# program 1 :- One-D random value using numpy
'''
import numpy as np
a  = np.random.randint(10,31,6)
print(a)
'''

# program 2 :- Two-D random value using numpy
'''
import numpy as np
a = np.random.random((3,3))
print(a)
'''

# find maximum and minimum value from 5x5 random value using numpy
'''
import numpy as np
arr = np.random.random((5,5))
print(arr)
arrmax, arrmin = arr.max(), arr.min()
print("Maximum value:-  " ,arrmax)
print("Minmum VAlue:-  ", arrmin)'''

# Program to find n largest value from array

import numpy as np
x = np.arange(13)
print("Original array:")
print(x)
np.random.shuffle(x)
n = 1
print (x[np.argsort(x)[-n:]])
