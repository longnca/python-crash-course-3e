# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and print a message for each order, such as "I made your tuna sandwich".
# As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

# Make a list
sandwich_orders = ['tuna', 'chicken', 'grilled cheese', 'ham', 'club', 'submarine']

# Make an empty list
finished_sandwiches = []

# Loop through the sandwich list
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    
    # Move to the finished_sandwiches list
    finished_sandwiches.append(sandwich)

# Print the finished sandwich list
print("\nThe following sandwiches have been made:")
for each in finished_sandwiches:
    print(each.title())
