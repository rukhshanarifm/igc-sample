#!/usr/bin/env python
"""Quick test of the feeder lines generator."""

import sys
print("Python path:", sys.executable)
print("Python version:", sys.version)

print("\nTesting imports...")
try:
    import geopandas as gpd
    print("✓ geopandas imported")
except ImportError as e:
    print(f"✗ geopandas import failed: {e}")
    sys.exit(1)

try:
    from shapely.geometry import Point, LineString, Polygon
    print("✓ shapely imported")
except ImportError as e:
    print(f"✗ shapely import failed: {e}")
    sys.exit(1)

try:
    from generate_feeder_lines import FeederLineGenerator
    print("✓ FeederLineGenerator imported")
except ImportError as e:
    print(f"✗ FeederLineGenerator import failed: {e}")
    sys.exit(1)

print("\nLoading UC data...")
try:
    generator = FeederLineGenerator("data/geo/geojson/union_councils.geojson")
    print(f"✓ Loaded {len(generator.gdf)} Union Councils")
except Exception as e:
    print(f"✗ Failed to load UC data: {e}")
    sys.exit(1)

print("\nGenerating test feeder lines...")
try:
    lines = generator.generate_feeder_lines_for_uc(uc_index=0, num_lines=2, num_segments=2)
    print(f"✓ Generated {len(lines)} feeder lines for UC 0")
    print(f"  First line: {lines[0]['properties']}")
except Exception as e:
    print(f"✗ Failed to generate feeder lines: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\nAll tests passed! ✓")
