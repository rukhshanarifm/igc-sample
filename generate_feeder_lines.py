"""
Generate random feeder lines within Union Council (UC) polygon boundaries.

This script reads UC boundaries from a GeoJSON file and generates random
feeder lines that stay within UC polygon areas.
"""

import json
import random
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Any

import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import unary_union
import numpy as np


class FeederLineGenerator:
    """Generate random feeder lines within UC polygon boundaries."""

    def __init__(self, geojson_path: str):
        """
        Initialize the generator with UC GeoJSON data.

        Args:
            geojson_path: Path to the union_councils.geojson file
        """
        self.geojson_path = Path(geojson_path)
        self.gdf = None
        self.load_uc_data()

    def load_uc_data(self):
        """Load UC data from GeoJSON file."""
        print(f"Loading UC data from {self.geojson_path}...")
        self.gdf = gpd.read_file(self.geojson_path)
        print(f"Loaded {len(self.gdf)} Union Councils")
        print(f"Columns: {self.gdf.columns.tolist()}")

    def point_in_polygon(self, point: Point, polygon: Polygon) -> bool:
        """
        Check if a point is within a polygon.

        Args:
            point: Shapely Point object
            polygon: Shapely Polygon object

        Returns:
            True if point is in polygon, False otherwise
        """
        return polygon.contains(point)

    def get_polygon_bounds(self, polygon: Polygon) -> Tuple[float, float, float, float]:
        """
        Get the bounding box of a polygon.

        Args:
            polygon: Shapely Polygon object

        Returns:
            Tuple of (minx, miny, maxx, maxy)
        """
        bounds = polygon.bounds
        return bounds

    def generate_random_point_in_polygon(self, polygon: Polygon) -> Point:
        """
        Generate a random point within a polygon using rejection sampling.

        Args:
            polygon: Shapely Polygon object

        Returns:
            A Point that lies within the polygon
        """
        minx, miny, maxx, maxy = self.get_polygon_bounds(polygon)
        
        while True:
            # Generate random point within bounding box
            random_x = random.uniform(minx, maxx)
            random_y = random.uniform(miny, maxy)
            point = Point(random_x, random_y)
            
            # Check if point is in polygon
            if self.point_in_polygon(point, polygon):
                return point

    def generate_random_line_in_polygon(
        self, polygon: Polygon, num_segments: int = 2
    ) -> LineString:
        """
        Generate a random line within a polygon.

        Args:
            polygon: Shapely Polygon object
            num_segments: Number of segments in the line (default 2 for simple lines)

        Returns:
            A LineString that lies within the polygon
        """
        points = []
        for _ in range(num_segments):
            point = self.generate_random_point_in_polygon(polygon)
            points.append((point.x, point.y))
        
        return LineString(points)

    def generate_feeder_lines_for_uc(
        self, uc_index: int, num_lines: int = 5, num_segments: int = 2
    ) -> List[Dict[str, Any]]:
        """
        Generate feeder lines for a specific Union Council.

        Args:
            uc_index: Index of the UC in the GeoDataFrame
            num_lines: Number of feeder lines to generate
            num_segments: Number of segments per line

        Returns:
            List of GeoJSON-compatible feature dictionaries
        """
        uc_row = self.gdf.iloc[uc_index]
        polygon = uc_row.geometry
        uc_name = uc_row.get('uc_name', f"UC_{uc_index}")
        uc_id = uc_row.get('uc_id', uc_index)

        feeder_lines = []
        for line_num in range(num_lines):
            line = self.generate_random_line_in_polygon(polygon, num_segments)
            
            feature = {
                "type": "Feature",
                "properties": {
                    "feeder_id": f"{uc_id}_{line_num}",
                    "uc_id": uc_id,
                    "uc_name": uc_name,
                    "line_number": line_num,
                    "coordinates_count": len(line.coords),
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": list(line.coords),
                },
            }
            feeder_lines.append(feature)

        return feeder_lines

    def generate_all_feeder_lines(
        self,
        num_lines_per_uc: int = 5,
        num_segments_per_line: int = 2,
        uc_indices: List[int] = None,
    ) -> Dict[str, Any]:
        """
        Generate feeder lines for all Union Councils.

        Args:
            num_lines_per_uc: Number of lines per UC (default 5)
            num_segments_per_line: Number of segments per line (default 2)
            uc_indices: List of specific UC indices to process. If None, process all.

        Returns:
            GeoJSON FeatureCollection with all feeder lines
        """
        if uc_indices is None:
            uc_indices = range(len(self.gdf))

        all_features = []
        total_ucs = len(uc_indices)

        for idx, uc_idx in enumerate(uc_indices):
            if idx % max(1, total_ucs // 10) == 0:
                print(f"Processing UC {idx + 1}/{total_ucs}...")

            try:
                lines = self.generate_feeder_lines_for_uc(
                    uc_idx, num_lines_per_uc, num_segments_per_line
                )
                all_features.extend(lines)
            except Exception as e:
                print(f"Error processing UC {uc_idx}: {e}")
                continue

        geojson_output = {
            "type": "FeatureCollection",
            "features": all_features,
        }

        print(f"Generated {len(all_features)} feeder lines")
        return geojson_output

    def save_to_geojson(self, geojson_data: Dict[str, Any], output_path: str):
        """
        Save generated feeder lines to a GeoJSON file.

        Args:
            geojson_data: GeoJSON FeatureCollection dictionary
            output_path: Path to save the GeoJSON file
        """
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w") as f:
            json.dump(geojson_data, f, indent=2)

        print(f"Saved feeder lines to {output_file}")

    def save_to_shapefile(
        self, geojson_data: Dict[str, Any], output_path: str
    ):
        """
        Save generated feeder lines to a Shapefile.

        Args:
            geojson_data: GeoJSON FeatureCollection dictionary
            output_path: Path to save the Shapefile (without extension)
        """
        # Convert GeoJSON to GeoDataFrame
        features = geojson_data["features"]
        geometries = [
            LineString(feature["geometry"]["coordinates"]) for feature in features
        ]
        properties = [feature["properties"] for feature in features]

        gdf = gpd.GeoDataFrame(properties, geometry=geometries)
        
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Shapefile requires .shp extension
        shapefile_path = str(output_file.with_suffix('.shp'))
        gdf.to_file(shapefile_path)

        print(f"Saved feeder lines to Shapefile: {shapefile_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate random feeder lines within UC polygon boundaries"
    )
    parser.add_argument(
        "geojson_path",
        type=str,
        help="Path to the union_councils.geojson file",
    )
    parser.add_argument(
        "--output-geojson",
        type=str,
        default="feeder_lines.geojson",
        help="Output GeoJSON file path (default: feeder_lines.geojson)",
    )
    parser.add_argument(
        "--output-shapefile",
        type=str,
        default=None,
        help="Output Shapefile path without extension (optional)",
    )
    parser.add_argument(
        "--lines-per-uc",
        type=int,
        default=5,
        help="Number of feeder lines per UC (default: 5)",
    )
    parser.add_argument(
        "--segments-per-line",
        type=int,
        default=2,
        help="Number of segments per feeder line (default: 2)",
    )
    parser.add_argument(
        "--uc-count",
        type=int,
        default=None,
        help="Limit to process only first N Union Councils (optional)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility (optional)",
    )

    args = parser.parse_args()

    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)
        np.random.seed(args.seed)
        print(f"Using random seed: {args.seed}")

    # Initialize generator
    generator = FeederLineGenerator(args.geojson_path)

    # Determine UC indices to process
    uc_indices = None
    if args.uc_count is not None:
        uc_indices = list(range(min(args.uc_count, len(generator.gdf))))
        print(f"Processing first {len(uc_indices)} Union Councils")

    # Generate feeder lines
    print(f"\nGenerating feeder lines...")
    print(f"  Lines per UC: {args.lines_per_uc}")
    print(f"  Segments per line: {args.segments_per_line}")
    
    geojson_data = generator.generate_all_feeder_lines(
        num_lines_per_uc=args.lines_per_uc,
        num_segments_per_line=args.segments_per_line,
        uc_indices=uc_indices,
    )

    # Save outputs
    generator.save_to_geojson(geojson_data, args.output_geojson)

    if args.output_shapefile:
        generator.save_to_shapefile(geojson_data, args.output_shapefile)

    print("\nDone!")


if __name__ == "__main__":
    main()
