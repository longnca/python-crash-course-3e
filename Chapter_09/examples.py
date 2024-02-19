# EXAMPLES OF OOP

# Defining a Class (Blueprint)
class Car:
    # Initializer with instance attributes
    def __init__(self, make, model, color):
        # Attributes to store car information
        self.make = make
        self.model = model
        self.color = color
    
    # Method to describe the car
    def describe(self):
        return f"{self.make} - {self.model} - {self.color}"
    
    # Method to repaint the car
    def paint(self, new_color):
        self.color = new_color
        return f"The car's new color is {new_color}."

# Creating Objects
my_car = Car('Honda', 'Civic', 'red')
dream_car = Car('Tesla', 'Model S', 'white')

# Using Methods and Attributes
print(my_car.describe()) # Output car details
print(dream_car.describe())

# Inheritance: Defining a subclass for Electric Cars
class ElectricCar(Car):
    # Initializer for ElectricCar, adding battery_size
    def __init__(self, make, model, color, battery_size):
        """Initialize attributes from the parent class"""
        super().__init__(make, model, color)
        self.battery_size = battery_size # New attribute for battery size
     
    # Method to show battery details
    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."

# Creating a new Object of ElectricCar and using its methods
my_electric_car = ElectricCar('Tesla', 'Model 3', 'red', 75)
print(my_electric_car.describe()) # Inherits and uses the describe method from Car parent class
print(my_electric_car.describe_battery()) # Output battery size