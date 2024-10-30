import random

words = ["python", "programming", "game", "fun", "hangman"]
secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print(" ".join(display_word))
    print(f"Attempts left: {attempts}")
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        
    elif guess in secret_word:
        print("Good guess!")
        guessed_letters.append(guess)
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break
    else:
        print("Wrong guess.")
        attempts -= 1
        guessed_letters.append(guess)
        
    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", secret_word)
