# Make a list containing a series of short text messages. 
# Pass the list ot a function called show_messages(), which prints each text message.

def show_messages(list):
    for msg in list:
        print(msg)
        
list = ['Hello!',
        'Welcome to Python Crash Course 3rd edition.',
        'I hope you to enjoy the book.']

show_messages(list)