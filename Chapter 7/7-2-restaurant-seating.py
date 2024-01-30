# Write a program that asks the user how many people are in the dinner group.
# If the answer is more than 8, print a message saying they'll have to wait for
# a table. Otherwise, report that their table is ready.

seating = input("How many are there in your group? ")

seating = int(seating) # convert string input to a numerical number

if seating > 8:
    print(f"Sorry, you'll have to wait for a table.")
else:
    print(f"Your table is ready.")


