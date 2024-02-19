# Start with your class from Exercise 9-1.
# Create three different instances from the class, 
# and call describe_restaurant() for each instance

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

# Create 3 instances
restaurant_1 = Restaurant('Harvest House', 'Western')
restaurant_2 = Restaurant('Hills Kitchen & Bar', 'Japanese')
restaurant_3 = Restaurant('Bell 720', 'Italian')

# Calling each instance
print(restaurant_1.describe_restaurant())
print(restaurant_2.describe_restaurant())
print(restaurant_3.describe_restaurant())