"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they
 enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their
 pizza.
"""
message="Please enter the pizza toppings you need: "
message+="\nEnter 'quit' when you want to exit: "
toppings=''
while(toppings != 'quit'):
    toppings = input(message)
    if toppings =='quit':
        break
    else:
        print(f"I will add {toppings} to your pizza")
