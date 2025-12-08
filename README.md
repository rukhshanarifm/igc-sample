# Pakistan Reform Tracking Dashboard

**A comprehensive web-based platform for monitoring government reform initiatives, analyzing sector performance, and exploring AI/ML research applications in Pakistan's power and tax sectors.**

[![Status: Active](https://img.shields.io/badge/status-active-success.svg)]()
[![Data: Demo](https://img.shields.io/badge/data-demonstration-orange.svg)]()

---

## 📋 Overview

This interactive dashboard system provides real-time visualization and deep-dive analysis of reform tracking across multiple sectors in Pakistan. Built with modern web technologies, it combines data visualization, geographic mapping, and comprehensive research summaries to support policy analysis and decision-making.

### Key Features

- 🔍 **Reform Tracking** - Monitor initiatives across Power and Tax sectors
- 📊 **Interactive Dashboards** - Real-time data visualization with D3.js and Plotly
- 🗺️ **Geographic Analysis** - District-level mapping with Leaflet.js
- 🤖 **AI Research Hub** - Literature reviews and technology applications
- 📈 **Deep Dive Reports** - Detailed analysis with policy recommendations

---

## 🚀 Quick Start

### 1. Run Local Server

```bash
cd /Users/rukhshanarifmian/igc-sample
python3 -m http.server 8000
```

### 2. Open in Browser

Navigate to: **http://localhost:8000**

The main portal (`index.html`) will automatically load with navigation to all sections.

---

## 📁 Project Structure

```
igc-sample/
├── index.html                          # Main entry point & portal
├── pages/
│   ├── reform_tracking.html            # Reform tracking hub
│   ├── sectors/
│   │   ├── power/
│   │   │   ├── power_sector.html       # Power sector landing
│   │   │   ├── power_deep_dive.html    # Power deep dive hub
│   │   │   └── net_metering_analysis.html  # Net-metering impact study
│   │   └── tax/
│   │       ├── tax_sector.html         # Tax reforms landing
│   │       ├── tax_deep_dive.html      # Tax deep dive hub
│   │       ├── fbr_risk_management.html    # FBR customs analysis
│   │       └── lahore_tax_potential.html   # Restaurant tax study
│   ├── dashboards/
│   │   ├── td_loss_dashboard.html      # T&D Loss interactive dashboard
│   │   └── tax_dashboard.html          # Tax revenue dashboard
│   └── ai/
│       ├── ai_research.html            # AI research hub
│       ├── ai_power_research.html      # Power sector AI applications
│       └── ai_tax_research.html        # Tax technology AI research
├── data/
│   ├── dummy/
│   │   ├── dummy_data.csv              # Power sector metrics
│   │   └── fbr_tax_data.csv            # Tax collection data
│   └── geo/
│       └── geojson/                    # Geographic boundary files
└── documentation/                       # Additional documentation
```

---

## 🎯 Main Sections

### 1. Reform Tracking

**Path:** `/pages/reform_tracking.html`

Central hub for monitoring reform initiatives:

#### Power Sector
- **Real-Time Dashboard** - T&D losses, recovery rates, circular debt visualization
- **Deep Dive Analysis:**
  - T&D Losses Analysis (17% national average, reduction strategies)
  - **Net-Metering Impact** - ₨10.2B annual revenue loss analysis
  - Recovery Rates Research (88% national, targeting 93%)
  - Circular Debt Analysis (2.84T PKR, structural reforms)

#### Tax Reforms
- **Real-Time Dashboard** - FBR collections, income tax trends, elasticity analysis
- **Deep Dive Analysis:**
  - Tax Burden Analysis (48% salaried class burden)
  - Income Elasticity Research (0.65 declining trend)
  - **FBR Risk Management** - Customs system optimization (70% false positive reduction)
  - **Lahore Tax Potential** - Restaurant enforcement study (₨3-5B potential)

### 2. AI Research Summary

**Path:** `/pages/ai/ai_research.html`

Comprehensive AI/ML research applications:

#### Power Sector AI
- T&D Loss Optimization (smart grid monitoring, predictive maintenance)
- Recovery Enhancement (84% accuracy defaulter prediction)
- Circular Debt Analysis (Bayesian causal models)

#### Tax Technology AI
- Property assessment automation (computer vision)
- Fraud detection systems
- Tax defaulter prediction models

---

## 📊 Interactive Dashboards

### T&D Loss Dashboard

**Path:** `/pages/dashboards/td_loss_dashboard.html`

**Features:**
- 📉 Time-series analysis of T&D losses by month
- 🗺️ District-level geographic mapping with overlay indicators
- 📈 Recovery rate vs. T&D loss correlation
- 🎯 Distribution analysis across DISCOs

**Key Visualizations:**
- Bar charts (monthly aggregation)
- Scatter plots (correlation analysis)
- Time series (trend detection)
- Interactive maps (district selection)

**Data Fixed:**
- ✅ Chronological month sorting (was alphabetical)
- ✅ User-friendly variable names ("T&D Loss" instead of "td_loss_dummy")
- ✅ Percentage formatting (15.2% instead of 0.152)

### Tax Dashboard

**Path:** `/pages/dashboards/tax_dashboard.html`

**Features:**
- 💰 FBR collection trends (FY 2010-2025)
- 📊 Income tax breakdown by source
- 📈 Tax elasticity analysis (declining from 1.42 to 0.65)
- 📉 Laffer Curve visualization (optimal rate analysis)

---

## 🔬 Deep Dive Studies

### Featured Analysis

#### 1. Net-Metering Impact Analysis
**Key Finding:** Households with net-metering reduce payments by 60% (₨29,000 → ₨12,000/month)

**Impact:**
- 50,000 connections nationwide
- ₨10.2B annual revenue loss
- Growing 35% annually

**Policy Recommendations:**
1. Implement "net billing" (wholesale export rates)
2. Fixed grid access charges (₨2,000-3,000/month)
3. Time-of-use net-metering

---

#### 2. FBR Risk Management System
**Problem:** 70% false positive rate in customs shipment classification

**Solution (IGC Intervention #3):**
1. Retrain ML model with 2020-2024 data
2. Implement trader trust score system
3. Dynamic threshold adjustment
4. Explainable AI dashboard for officers

**Expected ROI:**
- Investment: ₨500M
- Annual benefit: ₨8-10B
- Reduce clearance time: 2.5 days → 4 hours

---

#### 3. Lahore Restaurant Tax Enforcement
**Finding:** 86% non-compliance (7,300 out of 8,500 restaurants not filing)

**Revenue Potential:** ₨3-5B annually

**Strategy:**
- **Phase 1 (Q1 2025):** Targeted registration in Gulberg, DHA, Cantt
- **Phase 2 (Q2-Q3 2025):** Zone-based audit blitz
- **Phase 3 (Q4 2025+):** Real-time POS integration & compliance monitoring

---

## 🛠️ Technology Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **D3.js** | Data visualization | v7 |
| **Plotly.js** | Interactive charts | Latest |
| **Leaflet.js** | Geographic mapping | 1.9.4 |
| **HTML5/CSS3** | Frontend structure | - |
| **JavaScript** | Interactivity | ES6+ |
| **Python** | Data generation scripts | 3.8+ |

---

## 🎨 Design System

### Color Palette

```css
/* Primary Colors */
--primary-dark: #1B5E20;      /* Headers, footers */
--primary-medium: #2E7D32;    /* Accents, borders */
--primary-light: #81C784;     /* Buttons, highlights */

/* Backgrounds */
--bg-gradient-start: #f8faf9;
--bg-gradient-end: #f0f5f3;
--card-white: #ffffff;

/* Status Colors */
--success: #2E7D32;
--warning: #FF9800;
--danger: #D32F2F;
--info: #1976D2;
```

### Typography

- **Headers:** -apple-system, BlinkMacSystemFont, 'Segoe UI'
- **Weights:** 300 (light), 400 (regular), 600 (semibold), 700 (bold)
- **Sizes:** 0.9em to 3em (responsive scaling)

---

## 📦 Data Files

### Required CSV Data

1. **`data/dummy/dummy_data.csv`**
   - Power sector metrics (T&D losses, recovery rates, payments)
   - Monthly data by district and DISCO
   - Generated via `scripts/sample_data.py`

2. **`data/dummy/fbr_tax_data.csv`**
   - FBR tax collection data (FY 2010-2025)
   - Income tax breakdown by source
   - Generated via `scripts/generate_tax_data.py`

### GeoJSON Files

Located in `data/geo/geojson/`:
- `districts.geojson` - District boundaries
- `provinces.geojson` - Province boundaries
- `feeders.geojson` - Electricity feeder lines
- `union_councils.geojson` - UC boundaries by province
- `appended_district_analysis_completed.geojson` - District data with overlay indicators

---

## 🚦 Running the Project

### Method 1: Python HTTP Server (Recommended)

```bash
# Navigate to project directory
cd /Users/rukhshanarifmian/igc-sample

# Start server
python3 -m http.server 8000

# Open browser to:
# http://localhost:8000
```

### Method 2: Node.js HTTP Server

```bash
# Install http-server globally (one-time)
npm install -g http-server

# Run server
http-server -p 8000
```

### Method 3: Background Process

```bash
# Run in background
nohup python3 -m http.server 8000 > server.log 2>&1 &

# Stop server
pkill -f "http.server 8000"
```

---

## 🧪 Data Generation Scripts

Regenerate demonstration data:

```bash
# Power sector data
python3 scripts/sample_data.py

# Tax collection data
python3 scripts/generate_tax_data.py

# Feeder line data
python3 scripts/generate_feeder_data.py
```

---

## 🌐 Browser Compatibility

| Browser | Minimum Version | Status |
|---------|----------------|--------|
| Chrome | 90+ | ✅ Fully Supported |
| Firefox | 88+ | ✅ Fully Supported |
| Safari | 14+ | ✅ Fully Supported |
| Edge | 90+ | ✅ Fully Supported |
| IE | - | ❌ Not Supported |

---

## 🐛 Troubleshooting

### CORS Errors

**Problem:** Data not loading due to CORS policy

**Solution:** Always run through HTTP server, never open as `file://`

```bash
python3 -m http.server 8000
```

### Maps Not Displaying

**Checklist:**
1. ✅ Verify GeoJSON files exist in `data/geo/geojson/`
2. ✅ Check browser console (F12) for 404 errors
3. ✅ Ensure Leaflet library loaded (check Network tab)
4. ✅ Validate GeoJSON format at [geojson.io](http://geojson.io)

### Data Not Loading

**Checklist:**
1. ✅ Confirm CSV files exist in `data/dummy/`
2. ✅ Check file paths match dashboard code
3. ✅ Verify HTTP server is running
4. ✅ Inspect console for parsing errors

### Navigation Not Working

**Checklist:**
1. ✅ Verify all HTML files in correct directories
2. ✅ Check relative paths in `href` attributes
3. ✅ Clear browser cache (Cmd+Shift+R on Mac)
4. ✅ Review `PATH_VERIFICATION_REPORT.md` for path structure

---

## 📚 Documentation

Additional documentation available in `/documentation/`:

- **`PATH_VERIFICATION_REPORT.md`** - Navigation path verification
- **`PROJECT_OVERVIEW.md`** - Comprehensive project documentation
- **`TAX_DASHBOARD_README.md`** - Tax dashboard details
- **`FEEDER_LINES_README.md`** - Feeder visualization documentation

---

## ⚠️ Important Notes

### Data Disclaimer

> ⚠️ **All data in this dashboard is demonstration/fictitious data created for conceptual purposes only.** It does not reflect official government statistics and is not endorsed by the Government of Pakistan.

### Purpose

This is a **proof-of-concept** platform designed to:
- Demonstrate data visualization capabilities
- Showcase interactive dashboard design
- Illustrate policy analysis frameworks
- Provide templates for real implementation

### Not Included

- Real government data (all data is generated)
- Authentication/authorization systems
- Backend API integration
- Database connectivity
- User management

---

## 🚀 Future Enhancements

Potential additions for production deployment:

- [ ] Real-time data API integration
- [ ] User authentication & role-based access
- [ ] Export functionality (PDF, Excel)
- [ ] Advanced filtering & search
- [ ] Mobile-responsive improvements
- [ ] Multi-language support (Urdu)
- [ ] Database backend (PostgreSQL/MongoDB)
- [ ] RESTful API endpoints
- [ ] Automated data refresh pipelines

---

## 📝 License

This is a demonstration project. For production use, ensure compliance with relevant data protection and government information policies.

---

## 👥 Contact & Support

For questions or issues related to this dashboard:
1. Check documentation in `/documentation/`
2. Review troubleshooting section above
3. Inspect browser console for errors
4. Verify all file paths and data files exist

---

## 🔄 Version History

- **v2.0** (Current) - Reorganized structure with multi-page navigation
- **v1.5** - Added AI research summaries and tax dashboard
- **v1.0** - Initial T&D Loss dashboard with geographic mapping

---

**Last Updated:** December 8, 2025
