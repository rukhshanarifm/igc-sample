import json
import random
import csv

# Generate dummy feeder data
feeders = []

# Feeder naming convention: FEEDER_[PROVINCE]_[DISTRICT]_[CODE]
provinces = ["Punjab", "Sindh", "Khyber Pakhtunkhwa", "Balochistan"]
districts = {
    "Punjab": ["Lahore", "Karachi", "Faisalabad", "Multan", "Rawalpindi"],
    "Sindh": ["Karachi", "Hyderabad", "Sukkur", "Larkana"],
    "Khyber Pakhtunkhwa": ["Peshawar", "Abbottabad", "Swat", "Mardan"],
    "Balochistan": ["Quetta", "Gwadar", "Zhob", "Nushki"]
}

feeder_id = 1
for province in provinces:
    for district in districts.get(province, []):
        # Create 5-10 feeders per district
        num_feeders = random.randint(5, 10)
        for i in range(num_feeders):
            feeder = {
                "feeder_id": f"FDR_{province[:3].upper()}_{district[:3].upper()}_{str(feeder_id).zfill(4)}",
                "feeder_code": feeder_id,
                "province": province,
                "district": district,
                "feeder_name": f"{district} Feeder {i+1}",
                "substations_fed": random.randint(3, 15),
                "consumers": random.randint(500, 5000),
                "circuit_length_km": round(random.uniform(5, 80), 2),
                "peak_load_mw": round(random.uniform(2, 25), 2),
                "total_units_received": round(random.uniform(50000, 500000), 0),
                "units_billed": round(random.uniform(40000, 450000), 0),
                "td_loss_percent": round(random.uniform(3, 35), 2),
                "technical_loss_percent": round(random.uniform(2, 8), 2),
                "non_technical_loss_percent": round(random.uniform(1, 27), 2),
                "recovery_percent": round(random.uniform(60, 98), 2),
                "line_type": random.choice(["11kV", "33kV", "132kV"]),
                "conductor_type": random.choice(["ACSR", "AAC", "AAAC"]),
                "transformer_count": random.randint(1, 8),
                "transformer_capacity_mva": round(random.uniform(1, 50), 2),
                "maintenance_status": random.choice(["Good", "Fair", "Poor"]),
                "last_maintenance_days_ago": random.randint(10, 365),
                "coordinates_lat": round(random.uniform(23.6, 37.1), 4),
                "coordinates_lon": round(random.uniform(60.9, 77.1), 4),
                "month": "Dec-2024",
                "year": 2024
            }
            feeders.append(feeder)
            feeder_id += 1

# Write to CSV
csv_file = "data/dummy/feeder_data.csv"
with open(csv_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=feeders[0].keys())
    writer.writeheader()
    writer.writerows(feeders)

print(f"Generated {len(feeders)} feeder records")
print(f"Saved to {csv_file}")

# Generate GeoJSON for feeders
features = []
for feeder in feeders:
    feature = {
        "type": "Feature",
        "properties": {
            "feeder_id": feeder["feeder_id"],
            "feeder_name": feeder["feeder_name"],
            "td_loss_percent": feeder["td_loss_percent"],
            "district": feeder["district"],
            "province": feeder["province"],
            "consumers": feeder["consumers"],
            "circuit_length_km": feeder["circuit_length_km"],
            "recovery_percent": feeder["recovery_percent"],
            "maintenance_status": feeder["maintenance_status"]
        },
        "geometry": {
            "type": "Point",
            "coordinates": [feeder["coordinates_lon"], feeder["coordinates_lat"]]
        }
    }
    features.append(feature)

geojson = {
    "type": "FeatureCollection",
    "features": features
}

geojson_file = "data/geo/geojson/feeders.geojson"
with open(geojson_file, 'w') as f:
    json.dump(geojson, f, indent=2)

print(f"Generated GeoJSON with {len(features)} feeders")
print(f"Saved to {geojson_file}")
