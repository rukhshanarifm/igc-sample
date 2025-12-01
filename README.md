# Government of Pakistan Dashboard Portal

A comprehensive dashboard system for tracking government reforms and AI research initiatives across Pakistan.

## Features

- **Main Portal** (`dashboard_main.html`): Navigation hub with Reform Tracking and AI Research Summary
- **T&D Loss & Property Tax Dashboard** (`index.html`): Interactive analysis with maps and overlays
- **Reform Tracking**: Power sector and tax reform monitoring
- **AI Research Summary**: Literature reviews and recent newspaper articles

## Color Theme

- **Primary Green**: #1B5E20 (Dark) to #2E7D32 (Medium)
- **Background**: Light green gradient (#f1f8f4 to #e8f5e9)
- **White**: Clean, modern interface

## How to Run

### Option 1: Python HTTP Server (Recommended)

```bash
cd /Users/rukhshanarifmian/igc-sample
python3 -m http.server 8000
```

Then open in your browser:
- Main Portal: http://localhost:8000/dashboard_main.html
- T&D Dashboard: http://localhost:8000/index.html

### Option 2: Node.js HTTP Server

```bash
cd /Users/rukhshanarifmian/igc-sample
npx http-server -p 8000
```

### Option 3: Using Python's built-in server with background process

```bash
cd /Users/rukhshanarifmian/igc-sample
nohup python3 -m http.server 8000 > server.log 2>&1 &
```

To stop the server:
```bash
pkill -f "http.server 8000"
```

## File Structure

- `dashboard_main.html` - Main navigation portal
- `index.html` - T&D Loss and Property Tax Dashboard with tabs
- `dashboard_v2.html` - Alternative dashboard version
- `data/dummy/dummy_data.csv` - Main dataset
- `data/geo/geojson/` - Geographic boundary files

## Data Files

The dashboard requires:
1. **CSV Data**: `data/dummy/dummy_data.csv` (with power sector metrics)
2. **GeoJSON Files**: Geographic boundaries in `data/geo/geojson/`

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Technologies Used

- D3.js v7 - Data visualization
- Plotly.js - Interactive charts
- Leaflet.js - Interactive maps
- HTML5 / CSS3 / JavaScript

## Notes

- All data is dummy/demonstration data
- The dashboard works best with an HTTP server (not file:// protocol)
- Geographic data requires proper GeoJSON format
- Charts and maps are fully responsive

## Troubleshooting

### CORS Error
If you see "CORS policy" error, you must run the dashboard through an HTTP server, not open it as a file.

### Data Not Loading
1. Check that `data/dummy/dummy_data.csv` exists
2. Ensure the HTTP server is running
3. Check browser console (F12) for errors

### Maps Not Showing
1. Verify GeoJSON files exist in `data/geo/geojson/`
2. Check file paths in the console
3. Ensure Leaflet library is loaded
