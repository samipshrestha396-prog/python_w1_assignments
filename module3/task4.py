# Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.



import random
random_num=random.randint(1,10)
while True:
    guess_num=int(input("Guess the number between ( 1 and 10): "))
    if guess_num > random_num:
        print("it is high! Better luck next time!")
    elif guess_num < random_num:
        print("it is low! Better luck next time!")
    elif guess_num == guess_num:
        print("well done! you get it!")
        # I can use break here if I have to stop the game after getting correct one