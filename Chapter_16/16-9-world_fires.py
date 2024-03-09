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
lats, lons, brights = [], [], []
for row in reader:
    try:
        lat = float(row[header_row.index('latitude')])
        lon = float(row[header_row.index('longitude')])
        bright = float(row[header_row.index('brightness')])
    except ValueError as e:
        print(f"Error: {e}")
    else: 
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

# Pull the value from metadata part of the GeoJSON file
title = "World Fires"

fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
        color=brights,
        color_continuous_scale='plasma', #Color scales: https://plotly.com/python/builtin-colorscales/ 
        labels={'latitude', 'longitude'},
        projection='natural earth',
    )
fig.show()