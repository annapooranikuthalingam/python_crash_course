"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more
guests to invite to dinner.

Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing
people that you found a bigger dinner table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list.
"""
guests=['Manu','Medha','Vedanth']
print(f'Initial list is : {guests}')
print("Manu can't make it for dinner.")
del guests[0]
guests.insert(0,'Arunith')
print(f'Modified list is : {guests}')
guests.insert(0,'Kannan')
guests.insert(2,'Karthi')
guests.append('Athu')
print(f'Modified list is : {guests}')
print()
for i in range(len(guests)):
    print(f'Hi {guests[i]}, Please join with me for dinner.')