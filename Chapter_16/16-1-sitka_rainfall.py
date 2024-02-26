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

# Extract dates and rainfall
dates, prcps = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    prcp = float(row[5])
    dates.append(current_date)
    prcps.append(prcp)

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='red')

# Format plot
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # make x-axis labels diagonally
ax.set_ylabel("Rainfall Precipitation (inches to hundredths)", fontsize=16) # Rainfall unit
ax.tick_params(labelsize=16)

plt.show()