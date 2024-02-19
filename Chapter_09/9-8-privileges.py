# Write a separate 'Privileges' class.
# The class should have one attribute, privileges, that stores a list of strings
# as described in Exercise 9-7. 
# Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.

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

   
class Privileges:
    """A class to store a list of privileges."""
    
    def __init__(self, privileges = None):
        """Initializer with attribute privileges containing a list."""
        if privileges is None:
            self.privileges = ["can add post", "can ban user", "can add user"]
        else:
            self.privileges = privileges
    
    def show_privileges(self):
        """Display a set of privileges."""
        print(f"The Admin's Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
            
class Admin(User):
    """Create a subclass Admin from the superclass User."""
    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize attributes of the parent class.
        Then init the attribute Privileges."""
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = Privileges()

admin_1 = Admin("Aaron", "Barry", 45, "Calgary", "Electrician")
print(admin_1.describe_user())
admin_1.privileges.show_privileges()