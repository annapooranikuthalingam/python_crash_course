"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the
following at least once:

Use a conditional test in the while statement to stop the loop.
Use an active variable to control how long the loop runs.
Use a break statement to exit the loop when the user enters a 'quit' value.
"""

#case1
message="Please enter the pizza toppings you need: "
message+="\nEnter 'quit' when you want to exit: "
toppings=''
while(toppings != 'quit'):
    toppings = input(message)
    if toppings =='quit':
        break
    else:
        print(f"I will add {toppings} to your pizza")

#case2
active=True
while(active):
    message = "Please enter the pizza toppings you need: "
    message += "\nEnter 'quit' when you want to exit: "
    toppings = input(message)
    if toppings =='quit':
        active=False
    else:
        print(f"I will add {toppings} to your pizza")


