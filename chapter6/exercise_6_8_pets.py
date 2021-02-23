"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary,
 include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next,
 loop through your list and as you do, print everything you know about each pet.
"""
pet_1={'name':'milo','type':'dog','owner_name':'tesa'}
pet_2={'name':'kity','type':'cat','owner_name':'tresa'}
pet_3={'name':'pup','type':'dog','owner_name':'mitr'}
pet_4={'name':'brownie','type':'dog','owner_name':'aubrie'}
pet_5={'name':'meow','type':'cat','owner_name':'wesa'}
pet_6={'name':'catty','type':'cat','owner_name':'kathy'}
pets=[pet_1,pet_2,pet_3,pet_4,pet_5,pet_6]

for i in range(len(pets)):
    print(f"Name is {pets[i]['name']}")
    print(f"Type is {pets[i]['type']}")
    print(f"Owner Name is {pets[i]['owner_name']}")
    print('\n')