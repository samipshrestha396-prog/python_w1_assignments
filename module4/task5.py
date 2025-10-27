# Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.

username = "python"
password = "rules"
attempt = 0
while attempt < 5:
    inp_user_name = input("Enter your user name:")
    inp_user_pw = input("Enter your password name:")
    if (username == inp_user_name) and (password == inp_user_pw):
        print("Welcome!")
        break  # we can simply understand that (attempt=5)
    else:
        print("Invalid user and password!")

        attempt += 1
if attempt == 5:
    print("Access denied!")