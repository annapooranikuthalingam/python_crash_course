"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami'
appears in the list at least three times. Add code near the beginning of your program to print a message
saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami'
 from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""
sandwich_orders=['pastrami','chicken sandwich','pastrami','veg sandwich','tuna sandwich','pastrami']
finished_sandwiches=[]
print("THe deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    order=sandwich_orders.pop()
    print(f"I made your {order}")
    finished_sandwiches.append(order)
print(finished_sandwiches)
