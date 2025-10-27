# Write a program that asks the user to enter the names of five cities one by on
# (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line,
# in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.

# Write a program that asks the user to enter the names of five cities one by on
# (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line,
# in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.


list = []
# i=0
# while i <5:
#     city_name=input("enter the name of city: ")

#     list.append(city_name)             # we can use here while loop to perform same task.
#     i+=1
for i in range(5):
    city_name = input("enter the name of city: ")
    list.append(city_name)

for city in list:
    print("-", city)



