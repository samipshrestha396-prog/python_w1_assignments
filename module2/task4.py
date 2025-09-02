# Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.

year=int(input("Enter the year: "))
if year % 400==0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year!")
elif year % 4==0:
    print("leap year")
else:
    print("Not a leap year!")