# Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
#
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.

gender=str(input("Enter your gender: "))
level=float(input("Enter your hemoglobin value(g/l): "))

if gender=="male":
    if level< 134:
        print("Your hemoglobin is low!")
    elif level < (134<=level<=167):
            print("Your hemoglobin is normal!")
    else:
            print("Your hemoglobin is high!")

if gender=="female" and 117<=level<=155:
    if level < 117:
         print("Your hemoglobin is low!")
    elif level< (117<=level<=155):
        print("Your hemoglobin is normal!")
    else:
        (print("Your hemoglobin is high! "))
