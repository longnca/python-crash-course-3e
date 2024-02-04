# An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class
# you wrote in Exercise 9-1 or 9-4. 
# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        
    def describe_flavor(self):
        return f"The flavors of this ice cream is {self.flavors}"

ice_cream = IceCreamStand('Thai Express', 'Thai')

ice_cream.describe_flavor()