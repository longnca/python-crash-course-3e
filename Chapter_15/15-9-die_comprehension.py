"""Refactor exercise 15-6 using List Comprehension instead of For loop"""

import plotly.express as px

from die import Die

# Create two D8
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list using list comprehension
results = [die_1.roll() + die_2.roll() for roll_num in range(10_000)]

# Analyze the results using list comprehension
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results
title = "Results of Rolling two D8"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=range(2, max_result+1), y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)

# Show the chart
fig.show()

