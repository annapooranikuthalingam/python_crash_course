"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner,
and you have space for only two guests.

Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite
only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you
can’t invite them to dinner.

Print a message to each of the two people still on your list, letting them know they’re still invited.

Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure
you actually have an empty list at the end of your program.
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

#exercise 3_7
print("\nI can only invite only two people for dinner.")
while(len(guests)>2):
    removed_guest=guests.pop()
    print(f"Sorry {removed_guest}, I can't invite your for dinner")

print()
for i in range(len(guests)):
    print(f'Hi {guests[i]}, Please join with me for dinner.')

del guests[1]
del guests[0]
print(f'Final list is : {guests}')