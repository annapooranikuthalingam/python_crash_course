"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute
called number_served with a default value of 0. Create an instance called restaurant from this class.
Print the number of customers the restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers that have been served.
Call this method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment the number of customers who’ve
been served. Call this method with any number you like that could represent how many customers were
served in, say, a day of business.
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

restaurant= Restaurant('McDonalds','American')
print(f"The restaurant {restaurant.restaurant_name} has served {restaurant.number_served} customers")
restaurant.number_served=10
print(f"The restaurant {restaurant.restaurant_name} has served {restaurant.number_served} customers")
restaurant.set_number_served(20)
print(f"The restaurant {restaurant.restaurant_name} has served {restaurant.number_served} customers")
restaurant.increment_number_served(5)
print(f"The restaurant {restaurant.restaurant_name} has served {restaurant.number_served} customers")