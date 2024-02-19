# An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class
# you wrote in Exercise 9-1 or 9-4. 
# Either version of the class will work; just pick the one you like better.
# Add an attribute called 'flavors' that stores a list of ice cream flavors.
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
    def __init__(self, restaurant_name, cuisine_type, flavors=''):
        super().__init__(restaurant_name, cuisine_type)
        if flavors is None:
            self.flavors = []
        else:
            self.flavors = flavors
    
    def add_flavor(self, flavor):
        """Add a flavor to the ice cream stand list."""
        self.flavors.append(flavor)

    def describe_flavor(self):
        """Describe the flavors available."""
        if self.flavors:
            flavors_string = ', '.join(self.flavors)
            return f"The available ice cream flavors are: {flavors_string}."
        else:
            return "No flavors available."

# Create 2 instances
ice_cream_1 = IceCreamStand('Thai Express', 'Thai', ['vanilla', 'mint', 'chocolate'])
print(ice_cream_1.describe_flavor())

ice_cream_2 = IceCreamStand("Bull's Eyes", "BBQ", ['neapolitan', 'strawberry'])
print(ice_cream_2.describe_flavor())

# Create an instance that does not have any flavors
ice_cream_3 = IceCreamStand("Bull's Eyes", "BBQ")
print(ice_cream_3.describe_flavor())