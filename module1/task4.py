# Write a program that asks the user for three integer numbers.
# -The program prints out the sum, product, and average of the numbers.

num_1=float(input("Enter your 1st number:"))
num_2=float(input("Enter your 2nd number:"))
num_3=float(input("Enter your 3rd number:"))
total_sum=(num_1+num_2+num_3)
product= num_1*num_2*num_3
ave=(num_1+num_2+num_3)/3
print(f"total sum of the numbers is:{total_sum:.3f}")
print(f"product of the numbers is:{product:.3f}")
print(f"average of the numbers is:{ave:.3f}")