# Pizza Toppings

# Write a loop that prompts the user to enter a series of pizza toppings 
# until they enter 'quit' value. As they enter each topping, print a message
# saying that you'll add that topping to their pizza.

prompt = "Enter names of toppings that you want to add: "
prompt += "\n(Enter 'quit' to stop adding.)"

message = ""

active = True # set a flag
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(f"We just add the topping {message.title()} to your pizza.")