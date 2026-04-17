# Import random module to generate random number
import random

# Display welcome message
print("hi welcome to the number guessing game")
print("you have 7 chances to guess the number lets start")

# Define lower and upper range
low = 1
high = 50

# Inform user about the range
print(f"\nyou have 7 chances to guess the number between {low} and {high} lets start")

# Generate a random number between low and high
num = random.randint(low, high)

# Total chances allowed
ch = 7

# Counter for chances used
chance_gone = 0

# Start loop until chances are exhausted
while chance_gone < ch:
    
    # Increase chance count
    chance_gone += 1
    
    # Take user guess
    guess = int(input("enter your guess "))

    # If guess is correct
    if guess == num:
        print(f"correct the number is {num} you guessed it in {chance_gone} attempts")
        break

    # If all chances are used and guess is still wrong
    elif chance_gone >= ch and guess != num:
        print(f"sorry the number was {num} better luck next time")

    # If guess is higher than the number
    elif guess > num:
        print("too high try a lower number")

    # If guess is lower than the number
    elif guess < num:
        print("too low try a higher number")