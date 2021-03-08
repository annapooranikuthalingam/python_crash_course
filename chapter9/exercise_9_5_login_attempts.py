"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3
(page 162). Write a method called increment_login_attempts() that increments the value of
login_attempts by 1. Write another method called reset_login_attempts() that resets the value of
login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() several times. Print the
value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0.
"""

class User():
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

user_1=User('David','Anderson',30,'California')
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")
user_1.reset_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")
