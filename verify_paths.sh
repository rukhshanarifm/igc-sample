#!/bin/bash

echo "=========================================="
echo "Path Verification Report"
echo "=========================================="
echo ""

# Function to check if a file exists
check_file() {
    local file=$1
    if [ -f "$file" ]; then
        echo "✅ EXISTS: $file"
        return 0
    else
        echo "❌ MISSING: $file"
        return 1
    fi
}

# Function to extract and verify links from an HTML file
verify_links_in_file() {
    local file=$1
    local base_dir=$(dirname "$file")
    
    echo ""
    echo "Checking: $file"
    echo "----------------------------------------"
    
    # Extract href links (excluding http/https links)
    grep -o "href=['\"][^'\"]*['\"]" "$file" | grep -v "http" | sed "s/href=['\"]//g" | sed "s/['\"]//g" | while read -r link; do
        # Skip anchor links and javascript
        if [[ "$link" == \#* ]] || [[ "$link" == javascript:* ]]; then
            continue
        fi
        
        # Resolve relative path
        if [[ "$link" == /* ]]; then
            # Absolute path from root
            target_file="$link"
        else
            # Relative path
            target_file="$base_dir/$link"
        fi
        
        # Normalize path (remove ../ and ./)
        target_file=$(cd "$(dirname "$target_file")" 2>/dev/null && pwd)/$(basename "$target_file") 2>/dev/null
        
        if [ -f "$target_file" ]; then
            echo "  ✅ $link → $target_file"
        else
            echo "  ❌ BROKEN: $link (expected: $target_file)"
        fi
    done
}

# Main verification
echo "1. Verifying Core Files"
echo "=========================================="
check_file "index.html"
check_file "pages/reform_tracking.html"

echo ""
echo "2. Verifying Power Sector Files"
echo "=========================================="
check_file "pages/sectors/power/power_sector.html"
check_file "pages/sectors/power/power_deep_dive.html"
check_file "pages/sectors/power/net_metering_analysis.html"

echo ""
echo "3. Verifying Tax Sector Files"
echo "=========================================="
check_file "pages/sectors/tax/tax_sector.html"
check_file "pages/sectors/tax/tax_deep_dive.html"
check_file "pages/sectors/tax/fbr_risk_management.html"
check_file "pages/sectors/tax/lahore_tax_potential.html"

echo ""
echo "4. Verifying Dashboard Files"
echo "=========================================="
check_file "pages/dashboards/td_loss_dashboard.html"
check_file "pages/dashboards/tax_dashboard.html"

echo ""
echo "5. Verifying AI Research Files"
echo "=========================================="
check_file "pages/ai/ai_research.html"
check_file "pages/ai/ai_power_research.html"
check_file "pages/ai/ai_tax_research.html"

echo ""
echo "6. Verifying Data Files"
echo "=========================================="
check_file "data/dummy/dummy_data.csv"
check_file "data/geo/geojson/appended_district_analysis_completed.geojson"

echo ""
echo ""
echo "=========================================="
echo "Link Verification (checking navigation)"
echo "=========================================="

# Verify links in key files
verify_links_in_file "index.html"
verify_links_in_file "pages/reform_tracking.html"
verify_links_in_file "pages/sectors/power/power_sector.html"
verify_links_in_file "pages/sectors/tax/tax_sector.html"
verify_links_in_file "pages/dashboards/td_loss_dashboard.html"
verify_links_in_file "pages/dashboards/tax_dashboard.html"
verify_links_in_file "pages/ai/ai_research.html"

echo ""
echo "=========================================="
echo "Verification Complete!"
echo "=========================================="
