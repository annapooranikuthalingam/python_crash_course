"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters. Randomly
select four numbers or letters from the list and print a message saying that any ticket matching
these four numbers or letters wins a prize.
"""

from random import choices

our_list=[1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']
print("Any ticket matching the below four numbers or letters wins a prize:")
lottery_win=choices(our_list,k=4)
print(lottery_win)