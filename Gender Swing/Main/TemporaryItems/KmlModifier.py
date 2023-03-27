import json

with open('Main/Statistics/AustraliaLGA3MB.geojson', 'r') as f:
    data = json.load(f)

features = []

for feature in data['features']:
    properties = {
        'LGA_CODE22': feature['properties']['LGA_CODE22'],
        'LGA_NAME22': feature['properties']['LGA_NAME22'],
        'STE_CODE21': feature['properties']['STE_CODE21'],
        'STE_NAME21': feature['properties']['STE_NAME21'],
        'AUS_CODE21': feature['properties']['AUS_CODE21'],
        'AUS_NAME21': feature['properties']['AUS_NAME21'],
        'AREASQKM': feature['properties']['AREASQKM'],
        'LOCI_URI21': feature['properties']['LOCI_URI21']
    }
    geometry = feature['geometry']
    new_feature = {
        'type': 'Feature',
        'properties': properties,
        'geometry': geometry
    }
    features.append(new_feature)

new_data = {
    'type': 'FeatureCollection',
    'features': features
}

with open('AustraliaLGA3MB_new.geojson', 'w') as f:
    json.dump(new_data, f)
