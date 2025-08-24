# Write a program that asks the user for the length and width of a rectangle.
# -The program then prints out the perimeter and area of the rectangle.
# -The perimeter of a rectangle is the sum of the lengths of each four sides.

length=float(input("Enter the length of rectangle:"))
breadth=float(input("Enter the breadth of rectangle:"))
unit=str(input("Enter the unit such as.{cm,m,km,miles,ft}:"))
p=2*(length+breadth)
a=length*breadth
print(f"The are of rectangle is:{a}",unit,"square")
print("The perimeter of rectangle is:",p,unit,"square")