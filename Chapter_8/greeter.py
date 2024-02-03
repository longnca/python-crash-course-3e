# Using a function with a while loop:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name

# while loop
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    # set a variable for first_name:
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    # set a variable for last_name:
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    # call the function:
    name = get_formatted_name(f_name, l_name)
    print(f"Hello, {name}!")