prompt = "Tell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

# Define a flag
active = True 

# While loop will check the condition of flag 'active'
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)