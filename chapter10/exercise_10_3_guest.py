"""
10-3. Guest: Write a program that prompts the user for their name. When they respond, write
their name to a file called guest.txt.
"""

response=input('Enter your name: ')
with open('guest.txt','a') as fileobject:
    fileobject.write(f"{response}\n")

