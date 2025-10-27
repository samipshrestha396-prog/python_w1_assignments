# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# # The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

def converter():
    volume = int(input("Enter the volume of gasoline: "))

    return volume * 3.785
while True:
    volume_litre = converter()
    if volume_litre<0:
        print("Volume can not be in negative!Thank you!")
        break
    else:
        print(volume_litre, "litre")
