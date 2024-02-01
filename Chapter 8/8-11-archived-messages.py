# Start with your work from Exercise 8-10.
# Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messsages.

def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop()
        print(f"The message to be sent is: {msg}")
        sent_messages.append(msg)
        
def show_completed_send(sent_messages):
    print("\nSent messages:")
    for sent_message in sent_messages:
        print(sent_message)

# List of messages
messages = ['Hello!',
            'Welcome to Python Crash Course 3rd edition.',
            'I hope you enjoy the book.']

# List to store sent messages
sent_messages = []

# Make a copy of messages list and pass it to the function
send_messages(messages[:], sent_messages)
show_completed_send(sent_messages)

# Verify the original messages list remains intact
print("\nOriginal messages list:")
for message in messages:
    print(message)
