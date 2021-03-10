"""
10-5. Programming Poll: Write a while loop that asks people why they like programming. Each time
 someone enters a reason, add their reason to a file that stores all the responses.
"""
flag=True
while flag:
    poll=input("Why do you like programming?: ")
    response=input("Do you want to continue? Y/N?: ")
    if response=='N':
        flag=False
    with open('programming_poll.txt','a') as fileobject:
        fileobject.write(f"{poll}\n")

