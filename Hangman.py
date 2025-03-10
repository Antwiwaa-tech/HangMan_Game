import random
import json

def load_json(file_path):
    """Load list of words from json for the guessing game."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if not isinstance(data, dict) or not data:
                raise ValueError("Invalid or empty JSON data.")
            return data
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: {file_path} contains invalid JSON.")
    except ValueError as e:
        print(f"Error: {e}")
    return None  # Return None if any error occurs

list_of_words = load_json("words.json")


def start_game():
    """Start the word guessing game."""
    
    if not list_of_words:  # Check if words loaded successfully
        print("Word list is empty or invalid. Exiting game...")
        return

    # Ensure the list has valid categories
    valid_categories = [cat for cat in list_of_words if list_of_words[cat]]
    if not valid_categories:
        print("No valid categories found in the word list. Exiting game...")
        return

    category = random.choice(valid_categories)
    word_list = list_of_words[category]

    # Ensure the category has words
    if not word_list:
        print(f"No words available in the category '{category}'. Exiting game...")
        return

    word = random.choice(word_list).lower()

    print(f"\nYour word is from the category: '{category}' ")

    attempts = 0
    correct_guesses = set()

    while attempts < 8: # The programs allows a maximum of 7 incorrect to terminate
        guess = input("\nEnter a letter: ").strip().lower()
        
        if guess == 'quit':
                print("Exiting game...")
                return

        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in correct_guesses:
            print("You've already guessed that letter!")
            continue

        if guess in word:
            correct_guesses.add(guess)
            print("Correct \u2705\u2705")  
        else:
            attempts += 1
            print(f"Wrong \u274C\u274C | Attempts left: {8 - attempts}")  

        # Check if player has guessed the full word
        if all(letter in correct_guesses for letter in word):
            print(f"\n\U0001F389 Congratulations! You guessed the word: {word} \U0001F44D")
        
            return
        
       

    print(f"\nGame Over! The correct word was: {word} \U0001F61E") 
    print("Play(1) or Exit(0)")
    
     
    
    

# Main menu to proceed with the program
def hangman_game():
    """Ask the player if they want to start the game."""
    while True:
        intro = input("Complete the Word \U0001F603. Are you Ready?? (yes/no): ").strip().lower()  

        if intro in ['yes', 'y']:
            start_game()
            break
        elif intro in ['no', 'n']:
            print("Exiting game...")
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")


if __name__ == '__main__':
    hangman_game()
