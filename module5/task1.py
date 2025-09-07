# Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.

import random
def dice_roll():
   return random.randint(1,6)
while True:
    roll= dice_roll()
    print("You rolled", roll)
    if roll==6:
        print("you got 6!")
        break