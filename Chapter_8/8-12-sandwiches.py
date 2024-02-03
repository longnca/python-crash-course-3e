# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many item as the function call provides,
# and it should print a summary of the sandwich that's being ordered.
# Call the function three times, using a different number of arguments each time.

def sandwich(*items):
    print("The sandwich that's being ordered has:")
    for item in items:
        print(f"- {item}")
        

sandwich('tuna')
sandwich('chicken', 'tuna', 'ketchup')
sandwich('ham', 'cheese')