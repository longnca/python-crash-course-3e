# Add an attribute called login_attempts to your User class from Exercise 9-3.
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User:
    # Intializer
    def __init__(self, first_name, last_name, age, location, occupation):
        # Attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0 # Initialize login_attempts
    
    def describe_user(self):
        """Return the informaiton of the User."""
        return f"The user's information: {self.first_name} {self.last_name} - {self.age} - {self.location} - {self.occupation} - Login attempts: {self.login_attempts}."

    def greet_user(self):
        """Return a message to welcome the user."""
        return f"Hello, {self.first_name}!"
    
    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0
        
# Create an instance
user_1 = User('Adam', 'Sandle', '50', 'New York', 'Actor')

# Increments the login_attempts several times
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
# Check the number of login_attempts
print(user_1.describe_user())

# Reset the login attempts
user_1.reset_login_attempts()
# Check if the login_attempts is set to 0
print(user_1.describe_user())