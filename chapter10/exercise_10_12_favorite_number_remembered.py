"""
10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file.
If the number is already stored, report the favorite number to the user. If not, prompt for the
user’s favorite number and store it in a file. Run the program twice to see that it works.
"""
import json

filename="favnumber.json"

def store_favorite_number():
    favorite=input("What is your favorite number: ")
    with open(filename,'w') as f:
        json.dump(favorite,f)

def number_already_stored():
    try:
        with open(filename) as f:
            number=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


favorite_number=number_already_stored()
if favorite_number:
    print(f"I know your favorite number! It's {favorite_number}")
else:
    store_favorite_number()


