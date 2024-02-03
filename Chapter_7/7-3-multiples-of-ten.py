# Multiples of Ten

# Ask the user for a number, and then report whether the number is a multiple
# of 10 or not.

number = input("Tell me a number and I'll tell you if this number is a multiple of 10 or not: ")

number = int(number) # convert the string input to a numerical value

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else: 
    print(f"The number {number} is a not multiple of 10.")
