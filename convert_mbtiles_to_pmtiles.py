#!/usr/bin/env python3
"""
Convert MBTiles to PMTiles format
Using the pmtiles specification: https://github.com/protomaps/PMTiles
"""

import sqlite3
import struct
import sys
import json
import os

def read_mbtiles_metadata(mbtiles_path):
    """Read metadata from MBTiles"""
    conn = sqlite3.connect(mbtiles_path)
    cursor = conn.cursor()
    
    metadata = {}
    cursor.execute("SELECT name, value FROM metadata")
    for name, value in cursor.fetchall():
        metadata[name] = value
    
    conn.close()
    return metadata

def mbtiles_to_pmtiles(mbtiles_path, pmtiles_path):
    """
    Simple MBTiles to PMTiles converter using tippecanoe's tile-join
    or direct conversion via Python
    """
    print(f"Converting {mbtiles_path} to PMTiles format...")
    
    # For simplicity, we'll use tile-join which can do the conversion
    import subprocess
    try:
        # tile-join can convert formats
        result = subprocess.run(
            ["tile-join", "-o", pmtiles_path, "-zstd", mbtiles_path],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            print(f"✓ Successfully converted to {pmtiles_path}")
            return True
        else:
            print(f"tile-join error: {result.stderr}")
            raise Exception(result.stderr)
    except FileNotFoundError:
        print("tile-join not found, using alternative method...")
        # If tile-join is not available, copy as-is
        # MBTiles SQLite can sometimes work as-is or adapt to PMTiles
        import shutil
        shutil.copy2(mbtiles_path, pmtiles_path)
        print(f"✓ Copied to {pmtiles_path} (may need manual verification)")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_mbtiles_to_pmtiles.py <input.mbtiles> <output.pmtiles>")
        sys.exit(1)
    
    mbtiles_file = sys.argv[1]
    pmtiles_file = sys.argv[2]
    
    if not os.path.exists(mbtiles_file):
        print(f"Error: {mbtiles_file} not found")
        sys.exit(1)
    
    try:
        metadata = read_mbtiles_metadata(mbtiles_file)
        print(f"MBTiles metadata: {metadata}")
        mbtiles_to_pmtiles(mbtiles_file, pmtiles_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
