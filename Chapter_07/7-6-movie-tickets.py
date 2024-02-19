# Use a break statement to exit the loop when the user enters a 'quit' value

prompt = "What is your age? "
prompt += "\n(Enter 'quit' to exit.)"

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        message = int(message)
        if message < 3:
            print(f"Your ticket is free.")
        elif 3 <= message <= 12:
            print(f"Your ticket price is $10.")
        else: 
            print(f"Your ticket price is $15.")