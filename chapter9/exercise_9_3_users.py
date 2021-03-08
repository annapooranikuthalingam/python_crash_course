"""9-3. Users: Make a class called User. Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.

Create several instances representing different users, and call both methods for each user."""

class User():
    def __init__(self,first_name,last_name,age,location):
        """Initialises the user attributes"""
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.location=location

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

user_1=User('David','Anderson',30,'California')
user_1.describe_user()
user_1.greet_user()

user_2=User('Alice','Terry',40,'Georgia')
user_2.describe_user()
user_2.greet_user()