# Import the function from name_function.py
from name_function import get_formatted_name 

print(f"Enter 'q' at any time to quit.")
while True:
    first = input("\nEnter your first name: ")
    if first == 'q':
        break
    last = input("Enter your last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")