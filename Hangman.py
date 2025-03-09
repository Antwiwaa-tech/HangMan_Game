import random
import json

def load_josn(file_path):
    """Load list of words for the guessing game"""
    try:
        with open(file_path, "r" ) as file:
            return json.load(file)
    except FileNotFoundError:  
        print(f"Error: {file_path} not found.")     
        return None
    except json.JSONDecodeError:
        print(f"Error: {file_path} contains invalid JSON")
        return None
    
list_of_words = load_josn("words.json")   


def game_started():
    category = random.choice(list(list_of_words.keys()))
    
    word = random.choice(list_of_words[category])
    
    print(f"\nYour word is from the category: '{category}' ")
    

    guess = input("Guess the word \n >>> ")
    attempts = 0
    attempts += 1
    while attempts != 5: 
        if guess[0:] not in word[0:]:
            print('Wrong\u274C\u274C')
        else:
            print('Correct\u2705\u2705')    
        
    
    
     

def start_game():
    intro= input("Complete the Word\U0001F600. Are you Ready?? ").lower()
    
    if intro == 'yes' or intro == 'y':
        game_started()
        
    elif intro == 'no' or intro == 'n':
        print("Existing game...")
        quit()  
        
    
start_game()    