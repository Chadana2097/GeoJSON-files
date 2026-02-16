#!/usr/bin/env python3
# Extract MBTiles to z/x/y.pbf folder structure
# Usage: python extract_mbtiles.py input.mbtiles output_dir
import sqlite3, os, sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python extract_mbtiles.py <mbtiles_file> [output_dir]")
    sys.exit(1)

mbtiles_path = sys.argv[1]
output_dir = sys.argv[2] if len(sys.argv) > 2 else "tiles"

conn = sqlite3.connect(mbtiles_path)
cursor = conn.cursor()

output_path = Path(output_dir)
output_path.mkdir(exist_ok=True)

cursor.execute("SELECT zoom_level, tile_column, tile_row, tile_data FROM tiles")
tiles_count = 0

for z, x, y, data in cursor.fetchall():
    tile_dir = output_path / str(z) / str(x)
    tile_dir.mkdir(parents=True, exist_ok=True)
    with open(tile_dir / f"{y}.pbf", "wb") as f:
        f.write(data)
    tiles_count += 1

conn.close()
print(f"Extracted {tiles_count} tiles to {output_dir}/")
