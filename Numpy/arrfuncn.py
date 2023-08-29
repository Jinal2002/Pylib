# program of 5 numpy functions:-

# import numpy as np
 
# in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
# print ("Input array : \n", in_array)
 
# round_off_values = np.around(in_array)
# print ("\nRounded values : \n", round_off_values)
 
 
# in_array = [.53, 1.54, .71]
# print ("\nInput array : \n", in_array)
 
# round_off_values = np.around(in_array)
# print ("\nRounded values : \n", round_off_values)
 
# in_array = [.5538, 1.33354, .71445]
# print ("\nInput array : \n", in_array)
 
# round_off_values = np.around(in_array, decimals = 3)
# print ("\nRounded values : \n", round_off_values)

# import numpy as np
# arr  = np.array([1,2,4,9,6,5,15,7,])

# print("Original array:-", arr)
# for i in np.arange(np.size(arr)):
#     if arr[i]%2 == 0:
#         arr[i] = 0

# print("Alter array:-" , arr)

# draw square in Python Turtle
# Python program to draw square
# using Turtle Programming
import turtle
skk = turtle.Turtle()

for i in range(4):
	skk.forward(50)
	skk.right(90)
	
turtle.done()
