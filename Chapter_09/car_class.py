class Car:
    # Constructor method to initialize new instances
    def __init__(self, color, make):
        self.color = color  # Attribute
        self.make = make    # Attribute

    # Method to display information about the car
    def show_description(self):
        print(f"This is a {self.color} {self.make}.")


# Creating instances of the Car class
car1 = Car("red", "Toyota")
car2 = Car("blue", "Ford")

# These are two different objects (instances) of the Car class.


# Using the show_description method on our instances
car1.show_description()  # Outputs: This is a red Toyota.
car2.show_description()  # Outputs: This is a blue Ford.
