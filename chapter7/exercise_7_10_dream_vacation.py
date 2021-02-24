"""
7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt
similar to If you could visit one place in the world, where would you go? Include a block of code that
prints the results of the poll.
"""
print("Polling starts")
poll_results={}
active=True
while active:
    name=input("What is your name?: ")
    response=input("If you could visit one place in the world, where would you go?: ")
    poll_results[name]=response
    next=input("Do you want to pass the poll to next person? say 'yes' or 'no': ")
    if next == 'no':
        active= False

print("-----Poll results-----")
print(poll_results)