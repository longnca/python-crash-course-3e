import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) # add color map

# Set chart title and label axis
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes of Values", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set the range for each axis
ax.axis([0, 5100, 0, 135_000_000_000])
ax.ticklabel_format(style='plain')

plt.show()