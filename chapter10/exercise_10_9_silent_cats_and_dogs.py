"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either
file is missing.
"""
try:
    with open("cats.txt") as fileobject:
        contents=fileobject.read()
except FileNotFoundError:
    pass
else:
    print("----cats.txt----")
    print(contents)

try:
    with open("dogs.txt") as fileobject:
        contents1=fileobject.read()
except FileNotFoundError:
    pass
else:
    print("----dogs.txt----")
    print(contents1)