#This project focuses on the use of while loop to create a number guessing game.

import random

num_gen = random.randrange(1, 51)

user_guess = int(input("Guess the number between 1 and 50: "))

while user_guess != num_gen:

    if user_guess == num_gen:
        print("Congratulations! You guessed the correct number.")
        break

    elif user_guess < num_gen:
        print("Your guess is too low. Try again.")
        user_guess = int(input("Guess the number between 1 and 50: "))

    else:
        print("Your guess is too high. Try again.")
        user_guess = int(input("Guess the number between 1 and 50: "))