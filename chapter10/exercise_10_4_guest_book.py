"""
10-4. Guest Book: Write a while loop that prompts users for their name. When they enter
their name, print a greeting to the screen and add a line recording their visit in a file called
guest_book.txt. Make sure each entry appears on a new line in the file.
"""
flag=True
while flag:
    name=input("Enter Your name: ")
    response=input("Do you want to continue? Y/N?: ")
    if response=='N':
        flag=False
    with open("guest_book.txt",'a') as fileobject:
        fileobject.write(f'{name}\n')
