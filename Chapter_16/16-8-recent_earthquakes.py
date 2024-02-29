"""
Link to download GeoJSON dataset: 
https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php 
"""

from pathlib import Path
import json
import plotly.express as px 

path = Path('Chapter_16/eq_data/2.5_week.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

# Pull the value from metadata part of the GeoJSON file
title = all_eq_data['metadata']['title']

fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='solar', #Color scales: https://plotly.com/python/builtin-colorscales/ 
        labels={'color':'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()