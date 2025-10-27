# Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers.
# Use a for loop.

import random
total_sum=0
roll=int(input("Enter the number of dice roll: "))
for i in range(roll):
    random1 = random.randint(1, 6)
    total_sum= total_sum+random1

print(total_sum)