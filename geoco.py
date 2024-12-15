import pandas as pd
import osmnx as ox

data = pd.read_csv("calii.csv")

data['full_address'] = data['Restaurant Street Address'] + ", " + data['Restaurant City'] + ", " + data['State']

def geocode_address_osmnx(address):
    try:
        location = ox.geocode(address)
        return location[0], location[1]
    except Exception as e:
        print(f"Error geocoding {address}: {e}")
        return None, None

coordinates = []
for address in data['full_address']:
    coords = geocode_address_osmnx(address)
    coordinates.append(coords)

data['latitude'] = [c[0] for c in coordinates]
data['longitude'] = [c[1] for c in coordinates]

output_path = 'outcoords.csv'
data.to_csv(output_path, index=False)

print(f"Geocoded data saved to: {output_path}")
