# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and moves each message
# to a new list called sent_messages as it's printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.

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
