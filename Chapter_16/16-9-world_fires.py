"""
The dataset contains information about fires burning in different locations 
around the globe, including the latitude, longitude, and brightness of each fire.

Using the data-processing work from the first part of this chapter and the
mapping work from this section, make a map that shows which parts of the world
are affected by fires.

Link to download the most recent dataset:
https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data
"""

from pathlib import Path
import csv
import plotly.express as px 


path = Path('Chapter_16/eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract the latitude, longitude, and brightness from the dataset
lats, longs, brights = [], [], []
for row in reader:
    try:
        lat = int(row[header_row.index('latitude')])
        long = int(row[header_row.index('longitude')])
        bright = int(row[header_row.index('brightness')])
    except ValueError:
        print(f"Missing values for location at latitude and longitude")
    else: 
        lats.append(lat)
        longs.append(long)
        brights.append(bright)