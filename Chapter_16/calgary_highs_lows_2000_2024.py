"""
Plot the high and low temps of Calgary from 2000 to 2024.
Dataset source: https://climatedata.ca/
"""

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


path = Path('Chapter_16/weather_data/climate_daily_calgary_2000_2024.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Print the headers
# print(header_row)

# Print the headers with index
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# Extract dates, and high and low temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
    try:
        high = int(row[14])
        low = int(row[35])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily High and Low Temperatures, 2021\nCalgary, AB"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()