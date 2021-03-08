"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called
IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or
Exercise 9-4 (page 167). Either version of the class will work; just pick the one you like better.
Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""

class Restaurant():
    """A simple restaurant class"""
    def __init__(self,name, cuisine):
        """ Initialise name and type"""
        self.restaurant_name=name
        self.cuisine_type=cuisine
        self.number_served=0

    def describe_restaurant(self):
        """Print the restaurant information"""
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The restaurant cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Prints the message of opening the restaurant"""
        print(f"The restaurant {self.restaurant_name} is open")

    def set_number_served(self,number):
        """will sets the number os customers served"""
        self.number_served=number

    def increment_number_served(self,number):
        """Increments the number of customers served in a day"""
        self.number_served+=number

class IceCreamStand(Restaurant):
    """A specific kind of restaurant"""
    def __init__(self,name,cuisine):
        """Initialise from parent class and add more specific attributes"""
        super().__init__(name,cuisine)
        self.flavors=['vanilla','chocolate']

    def display_flavors(self):
        """Displays the flavors in an icecreamstand"""
        print(f"Flavors list: {self.flavors}")

my_ice_cream=IceCreamStand('Ice','Desserts')
my_ice_cream.display_flavors()