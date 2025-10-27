# Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
r=float(input("Enter the radius :"))
unit=str(input("Enter unit such as{m,km,inch,miles,foot,cm:"))
Area=r**2*3.14
print(f"Area of circle:{Area:2f} {unit}","square")