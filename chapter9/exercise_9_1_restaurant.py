"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store
two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant()
that prints these two pieces of information, and a method called open_restaurant() that prints a
message indicating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attributes individually, and then
call both methods.
"""
class Restaurant():
    """A simple restaurant class"""
    def __init__(self,name, cuisine):
        """ Initialise name and type"""
        self.restaurant_name=name
        self.cuisine_type=cuisine

    def describe_restaurant(self):
        """Print the restaurant information"""
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The restaurant cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Prints the message of opening the restaurant"""
        print(f"The restaurant {self.restaurant_name} is open")


restaurant= Restaurant('McDonalds','American')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
