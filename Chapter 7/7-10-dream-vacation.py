# Write a program that polls users about their dream vacation. 
# Write a prompt similar to "If you could visit one place in the world, where would you go?"
# Include a block of code that prints the results of the poll.

responses = []

# Set a flag
polling_active = True

while polling_active:
    # Polling question
    location = input("If you could visit one place in the world, where would you go? ")
    
    # Store the response
    responses.append(location)
    
    # Exit the loop
    repeat = input("Would you like to another dream vacation? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n--- Polling Results: Your dream vacations are ---")
for each in responses:
    print(each)