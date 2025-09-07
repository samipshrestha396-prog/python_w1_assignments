# Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list,
# -call the function, and print out the value it returned.
def sum_number(number):
    total=0
    for i in number:
        total=total+i
    return total
user_input=[1,2,3,4,5,8,9]
value=sum_number(user_input)
print(value)









