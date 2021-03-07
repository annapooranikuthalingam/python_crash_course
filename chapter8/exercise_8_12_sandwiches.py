"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered. Call the function three times,
using a different number of arguments each time.
"""

def sandwiches(*ingredients):
    print("Your sandwich will have the below items:")
    for ingre in ingredients:
        print(ingre)

sandwiches('chicken','lettuce','tomato','cheese')
sandwiches('chicken','lettuce','tomato')
sandwiches('chicken','cheese')