"""
Make a class called Restaurant. The __init__() method for Restaurant should
store 2 attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
"""

class Restaurant:
    # Initializer with attributes
    def __init__(self, restaurant_name, cuisine_type):
        # Attributes to store information
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Return the name and cuisine type of the restaurant."""
        return f"{self.restaurant_name} - {self.cuisine_type}"
    
    def restaurant_open(self):
        """Return the info that the restaurant is open."""
        return f"{self.restaurant_name} is open today."

# Create an object
bistro = Restaurant('Thai Bistro', 'Thai')

# Print the information
print(bistro.describe_restaurant())
print(bistro.restaurant_open())