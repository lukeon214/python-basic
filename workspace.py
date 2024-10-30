import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Computer randomly selects a number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    # Infinite loop until player guesses the right number
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

def calculator_basic():
    num1 = int(input("Enter your fist number: "))
    num2 = int(input("Enter your second number: "))

    print("Choose a operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Devide")

    choice2 = int(input("Type a number of the operation you want to proced "))

    if choice2 == 1:
        result = num1 + num2
        print(result)
    elif choice2 == 2:
        result = num1 - num2
        print(result)
    elif choice2 == 3:
        result = num1 * num2
        print(result)
    elif choice2 == 4:
        if num2 == 0:
            print("Cant devide by zero!")
        else:
            result = num1 / num2
            print(result)
    else:
        print("Invalid input")


print("Choose a program")
print("1. Guessing Game")
print("2. Calculator")

choice = int(input("Input a number of the program you want to run: "))

if choice == 1:
    number_guessing_game()
elif choice == 2:
    calculator_basic()

else:
    print("Invalid input")
