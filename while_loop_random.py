import random

secret_number = random.randint(1, 10)  # Random number between 1 and 10
guess = 0 # Initial number

while guess != secret_number:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

print("Congrats! You guessed the number.")