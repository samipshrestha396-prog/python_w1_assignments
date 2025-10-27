# Write a program that asks the user to enter the cabin class of a cruise ship and
# then prints out a written description according to the list below. You must use an if/elif/else
# structure in your solution.
#
# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.

cabin_class= str(input("Enter the cabin class: "))
if cabin_class == "LUX" or "lux":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A" or "a":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B" or "b":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C" or "c":
    print("windowless cabin below the car deck.")