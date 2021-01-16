"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a
 new set of invitations. You’ll have to think of someone else to invite.

Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the
guest who can’t make it.Modify your list, replacing the name of the guest who can’t make it with the name of the
new person you are inviting. Print a second set of invitation messages, one for each person who is still in your list.
"""
guests=['Manu','Medha','Vedanth']
print(f'Initial list is : {guests}')
print("Manu can't make it for dinner")
del guests[0]
guests.insert(0,'Arunith')
print(f'Modified list is : {guests}')
for i in range(len(guests)):
    print(f'Hi {guests[i]}, Please join with me for dinner.')