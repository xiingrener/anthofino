import pandas as pd
import folium
from folium.plugins import HeatMap

data_with_coords = pd.read_csv("fullcoords.csv")
data_with_coords = data_with_coords.dropna(subset=['latitude', 'longitude'])

map_center = [data_with_coords['latitude'].mean(), data_with_coords['longitude'].mean()]
base_map = folium.Map(location=map_center, zoom_start=10)

heat_data = data_with_coords[['latitude', 'longitude']].values.tolist()

HeatMap(heat_data).add_to(base_map)

output_map_path = 'all designs map.html'
base_map.save(output_map_path)

output_map_path
