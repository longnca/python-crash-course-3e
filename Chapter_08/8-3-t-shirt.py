# Write a function called 'make_shirt()' that accepts a size and text of a message
# that should be printed on the shirt. The function should print a sentence 
# summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the message printed on the shirt is {text}.")

# positional arg:
make_shirt('M', 'Smell Like Teen Spirit')

# keyword arg:
make_shirt(text='Bohemian Rhapsody', size= 'L')