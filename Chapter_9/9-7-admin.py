# An administrator is a special kind of user.
# Write a class called 'Admin' that inherits from the 'User' class from Exercise 9-3 or 9-5.
# Add an attribute, 'privileges', that stores a list of strings like "can add post",
# "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator's set of privileges.
# Create an instance of Admin, and call your method.

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

class Admin(User):
    """Create a subclass Admin from the superclass User."""
    def __init__(self, first_name, last_name, age, location, occupation, privileges=None):
        """Initializer adding a new attribute privileges."""
        super().__init__(first_name, last_name, age, location, occupation)
        if privileges is None:
            self.privileges = ["can add post", "can ban user", "can add user"]
        else:
            self.privileges = privileges
    
    def show_privileges(self):
        """Display the admin's set of privileges."""
        print(f"The Admin's Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
    
# Create an instance
user_1 = Admin("Aaron", "Barry", 45, "Calgary", "Electrician")
print(user_1.describe_user())
user_1.show_privileges()