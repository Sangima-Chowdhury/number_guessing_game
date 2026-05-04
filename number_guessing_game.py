# Number guessing game mh GAMEPLAN


# Generate a random number between 1 and 100
# Ask thr user to make a guess
# If not a valid number
# print error mesage "Not a valid number, try again"
# If number <guess
# print "Too low, try again"
# If number >guess
# print "Too high, try again"
# Else
# print "Congratulations! You guessed the number!"

import random

print("Welcome to the Number Guessing Game!")

number_to_guess = random.randint(1, 100)
# Loop until the user guesses the number
while True:
    try:
        user_guess = int(input("Guess a number between 1 and 100:  "))
        if user_guess < number_to_guess:
            print("Too low, try again.")
        elif user_guess > number_to_guess:
            print("Too high, try again.")
        else:
            print("Congratulations! You guessed the number!")
            break
    except ValueError:
        print("Not a valid number, try again.")
