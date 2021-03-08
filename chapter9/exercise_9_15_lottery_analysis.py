"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery
you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers
until your ticket wins. Print a message reporting how many times the loop had to run to give you a
winning ticket
"""

from random import choices

our_list=[1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']
my_ticket=['C','A',4,8,5,2]

#print("Any ticket matching the below four numbers or letters wins a prize:")
lottery_win=choices(our_list,k=4)
count=1
while(lottery_win not in my_ticket):
    lottery_win=choices(our_list,k=4)
    print(lottery_win)
    count+=1
print(f"Total run: {count}")

