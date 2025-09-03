# Write a program that converts inches to centimeters until the user inputs a negative value.
# Then the program ends.

value = int(input("Enter the  value in inch: "))

while value >= 0:
    print(value, "inch", "is =", value * 2.54, "cm")

    value = int(input("Enter the  value in inch:"))
    if value < 0:
        print("Enter the +ve number! Thank you!")
        value = int(input("Enter the  value in inch:"))

