"""Write a separate program that reads in this value(from 10_11) and prints the message,
“I know your favorite number! It’s _____.”
"""

import json
filename="favnumber.json"
with open(filename) as f:
    number=json.load(f)
    print(f"I know your favorite number! It's {number}")