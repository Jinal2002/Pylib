# WAP to print  to 100 value using arange function
'''import numpy as np
arr = np.arange(1,101,1)
print(arr)'''

# WAP to find the closest value (to a given scalar) in an array using numpy

import numpy as np
x = np.arange(100)
print(" Original array:- \n", x)
a = np.random.uniform(0,100)
print("Value to compare:- ",a)
index = (np.abs(x-a)).argmin()
print("x[index]:- ", x[index])
