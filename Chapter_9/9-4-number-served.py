# Start with your program from Exercise 9-1.
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, 
# and then change this value and print it again.

class Restaurant:
    # Initializer with attributes
    def __init__(self, restaurant_name, cuisine_type):
        # Attributes to store information
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Return the name and cuisine type of the restaurant."""
        return f"{self.restaurant_name} - {self.cuisine_type}"
    
    def restaurant_open(self):
        """Return the info that the restaurant is open."""
        return f"{self.restaurant_name} is open today."
    
    def customers_served(self):
        """Return the number of customers served by the restaurant."""
        return f"The number of customers the restaurant served is {self.number_served}."
    
    def update_customers_served(self, number):
        """Update the number of customers served."""
        self.number_served = number

bistro_1 = Restaurant('Harvest House', 'Western')
print(bistro_1.describe_restaurant())
print(bistro_1.customers_served())

# Update the number of customers served
bistro_1.update_customers_served(20)
# Re-print the number of customers served after updating
print(bistro_1.customers_served())