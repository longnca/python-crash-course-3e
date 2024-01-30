# Use a break statement to exit the loop when the user enters a 'quit' value

prompt = "Enter names of toppings that you want to add: "
prompt += "\n(Enter 'quit' to stop adding.)"

message = ""

while message != 'quit':
    message = input(prompt)
    
    if message == 'quit':
        break
    else:
        print(f"We just add the topping {message.title()} to your pizza.")