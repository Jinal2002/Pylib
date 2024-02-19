# Write a Python function that takes a list of numbers as input and returns the count of even numbers in the list.

def even(num):
    count = 0
    for i in num:
        if i%2 == 0:
            count += 1
    return count

num =list(map(int, input("Enter a list of Numbers ").split()))

e_count = even(num)
print("The count of even numbers is: ", e_count)
