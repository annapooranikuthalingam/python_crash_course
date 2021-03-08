"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6.
Write a method called roll_die() that prints a random number between 1 and the number of sides
the die has. Make a 6-sided die and roll it 10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from random import randint

class Die():
    """This represents a Dice"""
    def __init__(self,sides):
        """Initilaise the sides"""
        self.sides=sides

    def roll_die(self):
        """Prints a random number"""
        print(randint(1,self.sides))

print("---Dice 1 -----")
dice_1=Die(6)
for i in range(10):
    dice_1.roll_die()

print("---Dice 2 -----")
dice_2=Die(10)
for i in range(10):
    dice_2.roll_die()

print("---Dice 3 -----")
dice_3=Die(20)
for i in range(10):
    dice_3.roll_die()