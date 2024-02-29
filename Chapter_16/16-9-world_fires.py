"""
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


# Extract dates, and high and low temperatures
lats, lons, brights = [], [], []
for row in reader:
    try:
        lat = int(row[0])
        lon = int(row[1])
        brightness = int(row[2])
    except ValueError:
        print(f"Missing data")
    else:
        lats.append(lat)
        lons.append(lon)
        brights.append(brightness)

# Pull the value from metadata part of the GeoJSON file
title = 'World Fire Map'

fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
        color=brights,
        color_continuous_scale='solar', #Color scales: https://plotly.com/python/builtin-colorscales/ 
        labels={'color':'Magnitude'},
        projection='natural earth',
    )
fig.show()