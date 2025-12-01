# Feeder Lines Generator

Generate random feeder lines within Union Council (UC) polygon boundaries from a GeoJSON file.

## Features

- **Point-in-Polygon Detection**: Uses rejection sampling to ensure all generated points/lines stay within UC boundaries
- **Flexible Output**: Supports both GeoJSON and Shapefile formats
- **Customizable**: Control number of lines per UC, line complexity, and processing limits
- **Reproducible**: Optional random seed for reproducible results
- **Progress Tracking**: Real-time progress updates during generation

## Installation

### Required Dependencies

```bash
pip install geopandas shapely pandas numpy
```

Or install from requirements (if available):

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Generate 5 random feeder lines for each Union Council:

```bash
python generate_feeder_lines.py data/geo/geojson/union_councils.geojson
```

### Advanced Usage

```bash
python generate_feeder_lines.py \
  data/geo/geojson/union_councils.geojson \
  --output-geojson output/feeder_lines.geojson \
  --output-shapefile output/feeder_lines \
  --lines-per-uc 10 \
  --segments-per-line 3 \
  --uc-count 100 \
  --seed 42
```

### Command Line Options

- **`geojson_path`** (required): Path to the union_councils.geojson file

- **`--output-geojson`** (default: `feeder_lines.geojson`): Output GeoJSON file path

- **`--output-shapefile`** (optional): Output Shapefile path without extension
  - If specified, both GeoJSON and Shapefile formats will be saved
  - Example: `--output-shapefile output/feeder_lines`

- **`--lines-per-uc`** (default: 5): Number of feeder lines to generate per UC

- **`--segments-per-line`** (default: 2): Number of segments per feeder line
  - 2 segments = simple line between two points
  - 3+ segments = more complex path with multiple waypoints

- **`--uc-count`** (optional): Limit processing to first N Union Councils
  - Useful for testing with a subset of data

- **`--seed`** (optional): Random seed for reproducible results
  - Example: `--seed 42`

## Output Format

### GeoJSON Output

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "feeder_id": "35044_0",
        "uc_id": "35044",
        "uc_name": "Hanna (H-65)",
        "line_number": 0,
        "coordinates_count": 2
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [[67.054, 30.230], [67.062, 30.215]]
      }
    }
  ]
}
```

### Shapefile Output

The Shapefile will contain the same feature attributes as the GeoJSON, organized into standard Shapefile components (.shp, .shx, .dbf, etc.).

## Examples

### Example 1: Quick Test with 10 UCs

```bash
python generate_feeder_lines.py \
  data/geo/geojson/union_councils.geojson \
  --uc-count 10 \
  --seed 123
```

### Example 2: Generate Complex Networks

Create more complex feeder line networks with 3 segments per line:

```bash
python generate_feeder_lines.py \
  data/geo/geojson/union_councils.geojson \
  --lines-per-uc 20 \
  --segments-per-line 3 \
  --seed 42
```

### Example 3: Full Generation with Both Formats

```bash
python generate_feeder_lines.py \
  data/geo/geojson/union_councils.geojson \
  --output-geojson output/feeder_lines.geojson \
  --output-shapefile output/feeder_lines_shp \
  --lines-per-uc 10
```

## How It Works

1. **Load UC Data**: Reads the GeoJSON file containing Union Council polygons
2. **For Each UC**:
   - Get the polygon geometry and bounding box
   - Generate random points using rejection sampling:
     - Generate random coordinates within the bounding box
     - Check if point is inside the polygon
     - Repeat until a valid point is found
   - Connect random points to form feeder lines
3. **Save Results**: Export generated feeder lines to GeoJSON and/or Shapefile formats

## Performance Notes

- Rejection sampling can be slow for irregularly-shaped or small polygons
- Larger `--segments-per-line` values increase processing time
- For large datasets, consider using `--uc-count` for testing first
- Using a fixed `--seed` helps with reproducibility and debugging

## Troubleshooting

### Import Errors

If you get import errors for geopandas or shapely:

```bash
pip install --upgrade geopandas shapely
```

### Memory Issues

For very large datasets, process in batches using `--uc-count`:

```bash
python generate_feeder_lines.py input.geojson --uc-count 100 --output-geojson output_part1.geojson
```

### Slow Generation

- Reduce `--lines-per-uc` for faster generation
- Reduce `--segments-per-line` for simpler lines
- Test with `--uc-count` first

## File Structure

```
igc-sample/
├── generate_feeder_lines.py      # Main script
├── FEEDER_LINES_README.md         # This file
├── data/
│   └── geo/
│       └── geojson/
│           └── union_councils.geojson  # Input UC boundaries
└── output/
    ├── feeder_lines.geojson      # Generated output
    └── feeder_lines_shp.*        # Optional Shapefile output
```

## API Usage

You can also use the script programmatically:

```python
from generate_feeder_lines import FeederLineGenerator

# Initialize
generator = FeederLineGenerator('data/geo/geojson/union_councils.geojson')

# Generate for specific UC
lines = generator.generate_feeder_lines_for_uc(uc_index=0, num_lines=10)

# Generate for all UCs
all_lines = generator.generate_all_feeder_lines(num_lines_per_uc=5)

# Save results
generator.save_to_geojson(all_lines, 'output.geojson')
generator.save_to_shapefile(all_lines, 'output_shp')
```

## License

Adjust according to your project's license.
