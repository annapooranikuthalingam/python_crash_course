"""This module has the admin and privilege class"""
from user import User

class Privileges():
    """Will have the privileges"""
    def __init__(self):
        """Initialises the attributes"""
        self.privileges=["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """dispalys the admin privileges """
        print(f"admin has the below privileges: {self.privileges}")

class Admin(User):
    """admin- a special kind of user"""
    def __init__(self,first_name,last_name,age,location):
        """initialises the parent class attributes and attributes specific to admin"""
        super().__init__(first_name,last_name,age,location)
        self.privileges=Privileges()
