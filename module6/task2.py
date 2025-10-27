# Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues until
# -the program gets the maximum number on the dice, which is asked from the user at the beginning.

import random

number_sides= int(input("enter the number of roll: "))
def dice_roll(sides):
    times = 0
    while True:
        rolls=random.randint(1,sides)
        print("you rolled:",rolls)
        times += 1
        if rolls==number_sides:
            print("you got your maximumm number!",number_sides,"at",times,"rolls!")

            break


dice_roll(number_sides)