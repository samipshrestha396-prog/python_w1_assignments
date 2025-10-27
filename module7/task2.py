# Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending
# on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another
# in any order. Use the set data structure to store the names.

names=set()
while True:
    user_input = input("Enter your name(Press enter to exit!): ")
    if user_input=="":
        break
    if user_input in names:
        print("Existing name")
    else:
        names.add(user_input)


if user_input=="":
    for name in  names:
        print(name)


# this is a slightly differet way!
names=set()
user_input=input("enter your name: ")
while user_input!="":

    if user_input in names:
        print("exixting")
    else:
        names.add(user_input)

    user_input = input("enter your name: ")

if user_input=="":
    for i in names:
        print(i)

