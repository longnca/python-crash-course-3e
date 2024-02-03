# Make a class called Restaurant. The __init__() method for Restaurant should
# store 2 attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of
# infromation, and a method caleld open_restuarant() that prints a message indicating
# that the restaurant is open.

class Restaurant:
    # Initializer with attributes
    def __init__(self, restaurant_name, cuisine_type):
        # Attributes to store information
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    # Method to print information
    def describe_restaurant(self):
        return f"{self.restaurant_name} - {self.cuisine_type}"
    
    # Method to indicate the restaurant is open
    def restaurant_open(self):
        return f"{self.restaurant_name} is open today."

# Create an object
bistro = Restaurant('Thai Bistro', 'Thai')

# Print the information
print(bistro.describe_restaurant())
print(bistro.restaurant_open())