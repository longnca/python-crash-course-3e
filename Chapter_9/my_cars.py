"""Importing multiple classes from a module (page 176)."""

from car import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())


"""Importing an entire Module (page 177)."""

import car

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

"""Importing a Module into a Module (page 178)."""
from car import Car 
from electric_car_page177 import ElectricCar as EC # alias

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())