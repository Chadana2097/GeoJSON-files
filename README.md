# Traffic Analysis - GeoJSON & Vector Tiles

Complete dataset for traffic analysis with geospatial data in GeoJSON format and optimized vector tiles for VC Map integration.

## 📂 Contents

### Source Data
- **traffic_Analysis_WFL1.geojson** - Original traffic analysis dataset (37 LineString features)
  - CRS: EPSG:4326 (WGS84)
  - Attribute: Join_Count (2–263)
  - Location: Munich, Germany (11.56°E, 48.15°N)

### Vector Tiles (Production Ready)
- **traffic_analysis.pmtiles** - PMTiles v3 format (0.42 KB)
  - Compression: zstd
  - Zoom levels: 12–18
  - Layer name: `traffic_analysis`
  - Ready for hosting on GitHub, CDN, or web server

- **traffic_analysis.mbtiles** - MBTiles intermediate format (72 KB)
  - Backup/reference format
  - Can be regenerated if needed

### Styling & Configuration
- **style.json** - Mapbox/MapLibre style specification
  - 5-class graduated styling on Join_Count attribute
  - Colors: Light Blue → Dark Blue → Green → Orange → Red
  - Line width: 5px, opacity: 80%

### Documentation & Tools
- **METADATA.json** - Technical specifications & tile metadata
- **QUICK_REFERENCE.md** - Quick start guide for VC Map integration
- **convert_mbtiles_to_pmtiles.py** - Python script for MBTiles↔PMTiles conversion

## 🎨 Graduated Classification

| Join_Count | Color | Hex | Description |
|---|---|---|---|
| 2–25 | Light Blue | #66b2ff | Low traffic |
| 26–45 | Dark Blue | #0066cc | Medium traffic |
| 46–75 | Green | #00aa00 | High traffic |
| 76–167 | Orange | #ff8c00 | Very high traffic |
| 168–263 | Red | #c80000 | Critical traffic |

## 🚀 Quick Start - VC Map Integration

### 1. Raw PMTiles Download URL
```
https://raw.githubusercontent.com/Chadana2097/GeoJSON-files/main/traffic_analysis.pmtiles
```

### 2. Updated Style JSON (use in VC Map)
```json
{
  "version": 8,
  "name": "Traffic Analysis - Graduated Styling",
  "sources": {
    "traffic-tiles": {
      "type": "vector",
      "tiles": ["pmtiles://https://raw.githubusercontent.com/Chadana2097/GeoJSON-files/main/traffic_analysis.pmtiles/{z}/{x}/{y}.pbf"],
      "minzoom": 12,
      "maxzoom": 18
    }
  },
  "layers": [
    {
      "id": "traffic-lines",
      "type": "line",
      "source": "traffic-tiles",
      "source-layer": "traffic_analysis",
      "paint": {
        "line-width": 5,
        "line-color": [
          "step",
          ["get", "Join_Count"],
          "#66b2ff", 26, "#0066cc", 46, "#00aa00", 76, "#ff8c00", 168, "#c80000"
        ],
        "line-opacity": 0.8
      }
    }
  ]
}
```

### 3. Add to VC Map Configuration
```json
{
  "name": "Traffic Analysis",
  "type": "VectorTilesLayer",
  "url": "https://raw.githubusercontent.com/Chadana2097/GeoJSON-files/main/style.json",
  "minZoom": 12,
  "maxZoom": 18,
  "visible": true
}
```

## 📊 Data Specifications

- **Format**: PMTiles v3 (Protocol Buffers, zstd compression)
- **Geometry Type**: LineString
- **Feature Count**: 37
- **Spatial Extent**: 11.564°E–11.572°E, 48.146°N–48.153°N
- **Attributes**: 9 (OBJECTID, Join_Count, Name, OriginID, DestinationID, DestinationRank, Total_Kilometers, Total_WalkTime, TARGET_FID)
- **Performance**: 0.42 KB compressed, loads on-demand by zoom level

## 🔧 Tile Generation Tools

Generated using:
- **tippecanoe v2.49.0** - GeoJSON to MBTiles conversion
- **tile-join** - MBTiles to PMTiles conversion
- **Platform**: WSL Ubuntu 22.04 LTS

### Regenerate Tiles (if GeoJSON changes)
```bash
# Via WSL Ubuntu:
tippecanoe -o traffic_analysis.mbtiles -z 18 -Z 12 -l traffic_analysis traffic_Analysis_WFL1.geojson
tile-join -o traffic_analysis.pmtiles -zstd traffic_analysis.mbtiles
```

## 🌐 Alternative Hosting Options

### Option 1: GitHub Raw URL (Current)
```
https://raw.githubusercontent.com/Chadana2097/GeoJSON-files/main/traffic_analysis.pmtiles
```
✓ Works for PMTiles with CORS support via raw.githubusercontent.com

### Option 2: GitHub Releases
1. Create a release in GitHub
2. Upload traffic_analysis.pmtiles as attachment
3. Use release download URL:
```
https://github.com/Chadana2097/GeoJSON-files/releases/download/v1.0.0/traffic_analysis.pmtiles
```

### Option 3: GitHub Pages
1. Create `/docs` folder
2. Copy traffic_analysis.pmtiles there
3. Enable GitHub Pages in Settings
4. URL: `https://chadana2097.github.io/GeoJSON-files/traffic_analysis.pmtiles`

### Option 4: External CDN
- Cloudinary, Bunny CDN, AWS S3, or similar service
- Provides better performance and caching

## ✨ Features

✓ Single vector tile layer (no layer splitting)  
✓ Declarative styling (Mapbox/MapLibre compatible)  
✓ ArcGIS-like graduated classification  
✓ CORS-enabled for web integration  
✓ Compact size (0.42 KB with compression)  
✓ All attributes preserved in tiles  
✓ Zoom levels 12–18 fully optimized  

## 📝 Use Cases

- **Traffic Flow Visualization** - See traffic density across corridors
- **Route Analysis** - Identify bottlenecks and high-traffic areas
- **Urban Planning** - Data-driven infrastructure decisions
- **Real-time Dashboards** - Integrate with VC Map for live monitoring

## ⚙️ Technical Notes

- **Source Layer Name**: `traffic_analysis` (must match in style JSON)
- **CRS**: EPSG:4326 (WGS84, standard for web maps)
- **Tile Format**: Protocol Buffers (PBF)
- **Compression**: zstd (better compression than gzip for tiles)
- **Vector Tile Extent**: 4096 (standard web mercator)

## 🔗 Related Resources

- [PMTiles Specification](https://github.com/protomaps/PMTiles)
- [Mapbox Style Specification](https://mapbox.com/mapbox-gl-js/style-spec/)
- [Tippecanoe Documentation](https://github.com/mapbox/tippecanoe)
- [virtualcityS YSTEMS Documentation](https://www.vc.systems/)

## 📄 License

Original GeoJSON data © traffic_Analysis_WFL1.geojson source
Vector tiles and documentation by Lenovo User

---

**Generated**: February 16, 2026  
**Tools**: tippecanoe v2.49.0, tile-join, PMTiles CLI  
**Status**: ✅ Production Ready