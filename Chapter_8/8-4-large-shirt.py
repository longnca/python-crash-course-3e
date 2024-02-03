# Large Shirts

# Modify the 'make_shirt()' function so that shirts are large by default with a message that reads 'I love Python'. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# Define 'make_shirt()' function to have default values for both size and message
def make_shirt(size='Large', text='I love Python'):
    print(f"The size of the shirt is {size} and the message printed on the shirt is '{text}'.")

# Create a large shirt with the default message
print("\nLarge shirt with default message:")
make_shirt()

# Create a medium shirt with the default message
print("\nMedium shirt with default message:")
make_shirt(size='Medium')

# Create a shirt of any size (e.g., Small) with a different message
print("\nSmall shirt with a custom message:")
make_shirt(size='Small', text='Python is awesome!')
