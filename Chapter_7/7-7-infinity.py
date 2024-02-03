# Write a loop that never ends, and run it.
# To end the loop, press Ctrl + C or close the window displaying the output.

prompt = "What is your age? "
prompt += "\n(Enter 'quit' to exit.)"

message = input(prompt) # This will cause the infinity loop

while True:
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