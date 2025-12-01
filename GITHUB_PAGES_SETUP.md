# GitHub Pages Configuration Guide

## Current Setup

Your project is now configured for GitHub Pages deployment with the following structure:

### Main Files

- **`index.html`** - This is the main entry point for GitHub Pages (formerly `dashboard_main.html`)
  - Government of Pakistan Dashboard Portal
  - Links to various dashboards and research initiatives
  
- **`td_loss_dashboard.html`** - T&D Loss and Property Tax Dashboard (formerly `index.html`)
  - Comprehensive analysis of transmission & distribution losses
  - Includes T&D vs Property Tax overlay analysis
  - Feeder analytics with LineString visualizations

## How GitHub Pages Works

When you push to GitHub and enable GitHub Pages:
1. GitHub automatically looks for `index.html` in the repository root
2. `index.html` is served as your main website (https://yourusername.github.io/igc-sample/)
3. Other HTML files can be accessed as subpages

## Navigation Setup

Both main pages now have a navigation bar at the top:

```
Home | T&D Loss Dashboard
```

- **Home** - Links to `index.html` (main dashboard portal)
- **T&D Loss Dashboard** - Links to `td_loss_dashboard.html` (detailed analytics)

## To Deploy to GitHub Pages

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Update main dashboard configuration for GitHub Pages"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repository settings
   - Scroll to "GitHub Pages" section
   - Select "Deploy from a branch"
   - Choose "main" branch and "/" (root) folder
   - Save

3. **Access your site:**
   - Main dashboard: `https://yourusername.github.io/igc-sample/`
   - T&D Loss dashboard: `https://yourusername.github.io/igc-sample/td_loss_dashboard.html`

## File Organization

```
igc-sample/
├── index.html                    # Main entry point ← GitHub Pages serves this
├── td_loss_dashboard.html        # T&D Loss & Property Tax Dashboard
├── dashboard_v2.html             # (Optional/archived)
├── data/
│   ├── dummy/
│   │   ├── dummy_data.csv
│   │   └── feeder_data.csv
│   └── geo/
│       └── geojson/
│           ├── feeders.geojson
│           ├── union_councils.geojson
│           ├── districts.geojson
│           └── provinces.geojson
└── [other files...]
```

## Key Features

### Main Dashboard (index.html)
- Government portal interface
- Navigation to different dashboards
- Reform tracking
- AI research summary

### T&D Loss Dashboard (td_loss_dashboard.html)
- **Dashboard Overview Tab**
  - Real-time T&D loss metrics
  - Unit-received vs billed analysis
  - Distribution charts
  
- **T&D vs Property Tax Overlay Tab**
  - Correlation analysis between T&D losses and property tax collection
  - Multi-layer map visualization
  - Analysis by property types
  
- **Feeder Analytics Tab**
  - Feeder lines colored by T&D loss percentage
  - LineString visualization with actual paths
  - High-loss identification (red lines for >25% loss)
  - Performance statistics

## Data Files

- **dummy_data.csv** - T&D loss and recovery metrics by UC/month
- **feeder_data.csv** - Individual feeder performance data
- **feeders.geojson** - Feeder lines as LineStrings (Point A to Point B paths)
- **union_councils.geojson** - UC polygon boundaries
- **districts.geojson** - District boundaries
- **provinces.geojson** - Province boundaries

## Notes

- All data is sample/dummy data for demonstration
- Maps use OpenStreetMap tiles (Leaflet)
- Charts use Plotly for interactive visualizations
- D3.js used for data manipulation
- Fully responsive design for mobile and desktop
