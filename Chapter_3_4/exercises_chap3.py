names = ['Long', 'Adam', 'Kyle', 'Betty', 'Charlie', 'Thao']

# Exercise 3-7 
print(f"I can only 2 people for dinner.")

pop_Adam = names.pop(1)
print(f"Sorry {pop_Adam}")

pop_Thao = names.pop(4)
print(f"Sorry {pop_Thao}")

pop_Kyle = names.pop(1)
print(f"Sorry Kyle")

print(f"You still can join the dinner, {names[0]}, {names[1]}, {names[2]}")