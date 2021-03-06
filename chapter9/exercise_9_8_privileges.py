"""
9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges,
that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this
class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin
and use your method to show its privileges.
"""

class Privileges():
    """Will have the privileges"""
    def __init__(self):
        """Initialises the attributes"""
        self.privileges=["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """dispalys the admin privileges """
        print(f"admin has the below privileges: {self.privileges}")

class User():
    """User"""
    def __init__(self,first_name,last_name,age,location):
        """Initialises the user attributes"""
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.location=location
        self.login_attempts=0

    def describe_user(self):
        """Prints the summary of user"""
        print("Following are the user details:")
        print(f"First name is : {self.first_name}")
        print(f"Last name is : {self.last_name}")
        print(f"Age is : {self.age}")
        print(f"Location is : {self.location}")

    def greet_user(self):
        """Greets the user"""
        print(f"Welcome {self.first_name} {self.last_name}!.Have a Good Day. ")

    def increment_login_attempts(self):
        """Increments the login attempts"""
        self.login_attempts+=1

    def reset_login_attempts(self):
        """Resets the login attempts to 0"""
        self.login_attempts=0

class admin(User):
    """admin- a special kind of user"""
    def __init__(self,first_name,last_name,age,location):
        """initialises the parent class attributes and attributes specific to admin"""
        super().__init__(first_name,last_name,age,location)
        self.privileges=Privileges()

admin_user=admin('David','Johnson',50,'WDC')
admin_user.privileges.show_privileges()