# Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

list = []

user_input = int(input("Enter the numbers (press enter to exit): "))

for i in range((user_input)):
    # if hamle input chai loop vitra ligyo vane range jati xa tya samma input magxa yo for loop ko case ma
    user_input = int(input("Enter the degits : "))

    if user_input == " ":
        break
    list.append(int(user_input))
    list.sort(reverse=True)  # if we want in asccending order then(list.sort)
print(list)


