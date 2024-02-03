# Movie Tickets

# A movie theater charges different ticket prices depending on a person's age.
# If a person is under the age of 3, the ticket is free; if they are between 3
# and 12, the ticket is $10; and if they are over 12, the ticket is $15. 
# Write a loop in which you ask users their age, and then tell them the cost of
# their movie ticket.

prompt = "What is your age? "
prompt += "\n(Enter 'quit' to exit.)"

active = True # set a flag
while active:
    message = input(prompt)  
    if message == 'quit':
        active = False
    else:
        message = int(message)
        if message < 3:
            print(f"Your ticket is free.")
        elif 3 <= message <= 12:
            print(f"Your ticket price is $10.")
        else: 
            print(f"Your ticket price is $15.")