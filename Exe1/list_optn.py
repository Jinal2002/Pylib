# Create an empty list called fruits_list.
fruits_list = []
print(fruits_list)                                                  #1

# Add "apple", "banana", "orange", "grape", and "mango" to the fruits_list.
fruits_list = ["apple", "banana", "orange", "grape", "mango"]       #2
print(fruits_list)
# Print the first, last, and second & third fruits in the list using slicing.
print(fruits_list[1:6:3] , fruits_list[2:4])                        #3

# Print the number of fruits in the list.
print(len(fruits_list))                                             #4                   

# Replace the third fruit with "pear" in the list.
fruits_list[2] = "pear"                                             #5                
print(fruits_list)

# Check if "apple" is present in the fruits_list and print the result.
if "apple" in fruits_list:                                          #6
    print("YES")

# Remove "banana" and the last fruit from the list.
print(fruits_list[:1] + fruits_list[2:-1])                          #7    

# Create another list additional_fruits with "watermelon" and "kiwi", then concatenate it with fruits_list.
additional_fruits = ["watermelon" ,"kiwi"]                          #8
fruits = additional_fruits + fruits_list
print(fruits)

# Sort the fruits_list in alphabetical order.
fruits.sort()                                                       #9
print(fruits)

# Count the number of times "kiwi" appears in the fruits_list.
print(fruits.count("kiwi"))                                         #10