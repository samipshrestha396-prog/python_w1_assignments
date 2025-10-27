#
# Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.
import random
random_1=random.randint(0,9)
random_2=random.randint(0,9)
random_3=random.randint(0,9)
print(random_1,random_2,random_3)

# a 4-digit code where each number is between 1 and 6.
random_1=random.randint(0,6)
random_2=random.randint(0,6)
random_3=random.randint(0,6)
random_4=random.randint(0,6)
print(f"{random_1}{random_2}{random_3}{random_4}")

