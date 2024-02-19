# Make a classs called User. 
# Create two attributes called first_name and last_name.
# And then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user's information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:
    # Intializer
    def __init__(self, first_name, last_name, age, location, occupation):
        # Attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
    
    def describe_user(self):
        """Return the informaiton of the User."""
        return f"The user's information: {self.first_name} {self.last_name} - {self.age} - {self.location} - {self.occupation}."

    def greet_user(self):
        """Return a message to welcome the user."""
        return f"Hello, {self.first_name}!"
    
# create instances
user_1 = User('Alice', 'Moore', '30', 'Toronto', 'Doctor')
user_2 = User('Charlie', 'Brown', '45', 'Calgary', 'Electrician')

# print the users

print(user_1.describe_user())
print(user_1.greet_user())
print("\n")
print(user_2.describe_user())
print(user_2.greet_user())