"""The module specifies the restaurant"""

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