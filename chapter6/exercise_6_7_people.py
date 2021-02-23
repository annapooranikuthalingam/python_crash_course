"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries
representing different people, and store all three dictionaries in a list called people. Loop through your
list of people. As you loop through the list, print everything you know about each person.
"""

person_1={'first_name':'izzie','last_name':'stevens','age':'28','city':'seattle'}
person_2={'first_name':'della','last_name':'Rock','age':'30','city':'california'}
person_3={'first_name':'david','last_name':'sam','age':'20','city':'chicago'}
people=[person_1,person_2,person_3]

for i in range(len(people)):
    print(f"First Name is {people[i]['first_name']}")
    print(f"Last Name is {people[i]['last_name']}")
    print(f"Age is {people[i]['age']}")
    print(f"City is {people[i]['city']}")
    print('\n')