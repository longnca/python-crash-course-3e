# Using the list "sandwich_orders" from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
# and then use a while loop to remove all occurences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

# Make a list
sandwich_orders = ['tuna', 'pastrami','chicken', 'pastrami', 'grilled cheese', 'pastrami', 'ham','club', 'submarine']

print("Sorry, we run out of pastrami sandwiches.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
print(sandwich_orders)