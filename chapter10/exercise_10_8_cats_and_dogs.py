"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats
in the first file and three names of dogs in the second file. Write a program that tries to read
these files and print the contents of the file to the screen. Wrap your code in a try-except block
to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the
files to a different location on your system, and make sure the code in the except block executes
properly.
"""
try:
    with open("cats.txt") as fileobject:
        contents=fileobject.read()
except FileNotFoundError:
    print("The file cats.txt is missing")
    pass
else:
    print("----cats.txt----")
    print(contents)

try:
    with open("dogs.txt") as fileobject:
        contents1=fileobject.read()
except FileNotFoundError:
    print("The file dogs.txt is missing")
    pass
else:
    print("----dogs.txt----")
    print(contents1)
