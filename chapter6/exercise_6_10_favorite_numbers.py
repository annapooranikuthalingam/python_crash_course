"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person can have more
than one favorite number. Then print each person’s name along with their favorite numbers.
"""

favorite_numbers={'david':[5,6,8],'alice':[7,10,4,2,1],'tesa':[3],'norman':[1,2,3],'tina':[5,3]}
for key, value in favorite_numbers.items():
    print(f"Favorite numbers of {key} is {value}")