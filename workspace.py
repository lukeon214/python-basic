import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Computer randomly selects a number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    # Infinite loop
    while True:
        # Get the player's guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

number_guessing_game()
