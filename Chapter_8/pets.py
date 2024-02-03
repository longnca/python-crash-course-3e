# Positional Arguments
print(f"\n1. Positional Arguments:")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a new {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

## Multiple function calls
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword Arguments 
print(f"\n2. Keyword Arguments:")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='Harry')
describe_pet(pet_name='Tom', animal_type='dog') # The order doesn't matter anymore