"""
In this section, we hardcoded the indexes corresponding to the TMIN and TMAX
columns. Use the header row to determine the indexes for these values, so your
program can work for Sitka or Death Valley. Use the station name to automatically
generate an appropriate title for your graph as well.
"""

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


path = Path('Chapter_16/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Print the headers
print(header_row)

# Print the headers with index
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates, and high and low temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
    try:
        high = int(row[header_row.index('TMAX')])
        low = int(row[header_row.index('TMIN')])
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

# Dynamic graph title
station_name = "Sitka"

# Format plot
ax.set_title(f"Daily High and Low Temperatures of {station_name}, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()  # make x-axis labels diagonally
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()