"""
Generate feeder lines as LineStrings (from point A to point B) instead of just Points.
Converts the feeder data to GeoJSON with proper line geometries.
"""

import json
import csv
import random
from pathlib import Path
import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two coordinates in km."""
    R = 6371  # Earth's radius in kilometers
    
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c

def generate_feeder_line(start_lat, start_lon, circuit_length_km, num_segments=5):
    """
    Generate a feeder line from a starting point.
    
    Args:
        start_lat, start_lon: Starting coordinates
        circuit_length_km: Total length of the feeder circuit
        num_segments: Number of waypoints in the line
    
    Returns:
        List of [lon, lat] coordinates representing the feeder line
    """
    coordinates = [[start_lon, start_lat]]
    
    current_lat = start_lat
    current_lon = start_lon
    remaining_distance = circuit_length_km
    
    for i in range(num_segments - 1):
        # Generate random direction (bearing)
        bearing = random.uniform(0, 360)
        bearing_rad = math.radians(bearing)
        
        # Distribute distance among segments
        segment_distance = remaining_distance / (num_segments - i)
        
        # Convert distance to approximate lat/lon change
        # Roughly 1 degree = 111 km
        lat_change = (segment_distance / 111) * math.cos(bearing_rad)
        lon_change = (segment_distance / (111 * math.cos(math.radians(current_lat)))) * math.sin(bearing_rad)
        
        new_lat = current_lat + lat_change
        new_lon = current_lon + lon_change
        
        coordinates.append([new_lon, new_lat])
        
        current_lat = new_lat
        current_lon = new_lon
        remaining_distance -= segment_distance
    
    return coordinates

def load_feeder_data(csv_path):
    """Load feeder data from CSV file."""
    feeders = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            feeders.append(row)
    return feeders

def generate_feeder_geojson(csv_path, output_path):
    """Generate feeder GeoJSON with LineString geometries."""
    
    # Load feeder data from CSV
    feeders = load_feeder_data(csv_path)
    print(f"Loaded {len(feeders)} feeder records from CSV")
    
    features = []
    
    for feeder in feeders:
        try:
            # Get coordinates from lat/lon in CSV
            lat = float(feeder.get('lat', 30.3753))
            lon = float(feeder.get('lon', 69.3451))
            circuit_length = float(feeder.get('circuit_length_km', 10))
            
            # Generate line coordinates
            line_coordinates = generate_feeder_line(lat, lon, circuit_length, num_segments=5)
            
            feature = {
                "type": "Feature",
                "properties": {
                    "feeder_id": feeder['feeder_id'],
                    "feeder_name": feeder['feeder_name'],
                    "uc_name": feeder['uc_name'],
                    "province": feeder['province'],
                    "district": feeder['district'],
                    "consumers": int(feeder.get('consumers', 0)),
                    "circuit_length_km": float(feeder.get('circuit_length_km', 0)),
                    "peak_load_mw": float(feeder.get('peak_load_mw', 0)),
                    "td_loss_percent": float(feeder.get('td_loss_percent', 0)),
                    "technical_loss_percent": float(feeder.get('technical_loss_percent', 0)),
                    "non_technical_loss_percent": float(feeder.get('non_technical_loss_percent', 0)),
                    "recovery_percent": float(feeder.get('recovery_percent', 0)),
                    "line_type": feeder.get('line_type', 'Unknown'),
                    "maintenance_status": feeder.get('maintenance_status', 'Unknown')
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": line_coordinates
                }
            }
            features.append(feature)
            
        except Exception as e:
            print(f"Error processing feeder {feeder.get('feeder_id', 'unknown')}: {e}")
            continue
    
    # Create FeatureCollection
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    
    # Save to file
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(geojson, f, indent=2)
    
    print(f"Generated {len(features)} feeder LineStrings")
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    csv_path = "data/dummy/feeder_data.csv"
    output_path = "data/geo/geojson/feeders.geojson"
    
    generate_feeder_geojson(csv_path, output_path)
    print("Feeder GeoJSON generation complete!")
