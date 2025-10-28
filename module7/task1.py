# Write a program that asks the user for a number of a month and then prints out the corresponding
# season (spring, summer, autumn, winter). Save the seasons as strings into a
# tuple in your program. We can define each season to last three months,
# December being the first month of winter.

user_input=int(input("Enter the number of month: "))
seasons=("spring","summer","autumn","winter")
if user_input in (12,1,2):
    print(seasons[3])
elif user_input in (3,4,5):
    print(seasons[0])
elif user_input in (6,7,8):
    print(seasons[1])
else:
    print(seasons[2])