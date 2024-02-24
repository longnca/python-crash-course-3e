"""Simulate the path of a pollen grain on the surface of a drop of water."""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:
    # Make a random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=3)
    ax.set_aspect('equal')

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break