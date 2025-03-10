import random
import json

def load_json(file_path):
    """Load list of words for the guessing game"""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:  
        print(f"Error: {file_path} not found.")     
        return None
    except json.JSONDecodeError:
        print(f"Error: {file_path} contains invalid JSON")
        return None

list_of_words = load_json("words.json")   

def game_started():
    if not list_of_words:  # Check if words loaded successfully
        print("Word list is empty. Exiting game...")
        return

    category = random.choice(list(list_of_words.keys()))
    word = random.choice(list_of_words[category])

    print(f"\nYour word is from the category: '{category}' ")
    
    attempts = 0
    correct_guesses = set()  # To track correct letters

    while attempts < 5:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter!")
            continue

        if guess in word:
            correct_guesses.add(guess)
            print('Correct \u2705"\u2705')
        else:
            attempts += 1
            print(f'Wrong \u274C\u274C | Attempts left: {5 - attempts}')

        # Check if the player has guessed all letters in the word
        if all(letter in correct_guesses for letter in word):
            print(f"Congratulations! You guessed the word: {word} \U0001F389\U0001F44D")
            return

    print(f"Game Over! The correct word was: {word} \U0001F61E")

def start_game():
    intro = input("Complete the Word \U0001F603. Are you Ready? (yes/no): ").lower()
    
    if intro in ['yes', 'y']:
        game_started()
    elif intro in ['no', 'n']:
        print("Exiting game...")
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")

start_game()
