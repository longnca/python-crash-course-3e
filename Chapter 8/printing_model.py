def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# The function of moving items between 2 lists:
print_models(unprinted_designs, completed_models)

# The function of showing the final list after moving:
show_completed_models(completed_models)

# REMEMBER: <page 145>
# Every function should have one specific job.
# This is more beneficial than using one function to do both jobs.
# If you're writing a function and notice the function is doing too many different tasks,
# try to split the code into two functions.