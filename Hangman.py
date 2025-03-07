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
    
     

def start_game():
    intro= input("Complete the Word\U0001F600. Are you Ready?? ").lower()
    
    if intro == 'yes' or intro == 'y':
        game_started()
        
    elif intro == 'no' or intro == 'n':
        quit()  
        
    
    