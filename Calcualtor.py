# Number Guessing Game

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user for a guess
guess = int(input("Guess a number between 1 and 10: "))

# Loop until the guess is correct
while guess != secret_number:
    if guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Try again: "))

print("Congratulations! You guessed it!")
