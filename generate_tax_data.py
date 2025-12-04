"""
Generate dummy FBR tax collection data for Pakistan Tax Dashboard
This creates realistic synthetic data with trends for:
- Total FBR collection by category
- Income tax breakdown by source
- Salaried class tax burden over time
- Laffer Curve dynamics
"""

import pandas as pd
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)

def generate_fbr_tax_data():
    """Generate comprehensive FBR tax collection dataset"""
    
    years = ['2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24', '2024-25']
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    months_map = {
        'Q1': ['Jul', 'Aug', 'Sep'],
        'Q2': ['Oct', 'Nov', 'Dec'],
        'Q3': ['Jan', 'Feb', 'Mar'],
        'Q4': ['Apr', 'May', 'Jun']
    }
    
    data = []
    
    for year_idx, year in enumerate(years):
        # Base growth factor (economy growing ~15% per year)
        base_growth = 1 + (year_idx * 0.15)
        
        # Tax rate increases over time
        tax_rate_multiplier = 1 + (year_idx * 0.08)
        
        for quarter_idx, quarter in enumerate(quarters):
            # Seasonal variation
            seasonal_factor = 1 + (quarter_idx * 0.05)
            
            # ---------- INCOME TAX COMPONENTS ----------
            
            # Salaried Class - increasing burden over time
            salaried_income_base = 150 + np.random.uniform(-20, 30)
            salaried_income = salaried_income_base * base_growth * seasonal_factor
            salaried_tax_rate = 15 + (year_idx * 1.5) + np.random.uniform(-1, 1)  # Increasing from 15% to ~22%
            salaried_tax = salaried_income * (salaried_tax_rate / 100)
            
            # Corporate Tax
            corporate_income_base = 300 + np.random.uniform(-50, 100)
            corporate_income = corporate_income_base * base_growth * seasonal_factor
            corporate_tax_rate = 29 + np.random.uniform(-1, 2)  # Around 29%
            corporate_tax = corporate_income * (corporate_tax_rate / 100)
            
            # Business Income Tax
            business_income_base = 200 + np.random.uniform(-40, 80)
            business_income = business_income_base * base_growth * seasonal_factor
            business_tax_rate = 20 + np.random.uniform(-2, 3)  # Around 20%
            business_tax = business_income * (business_tax_rate / 100)
            
            # Capital Gains Tax
            capital_gains_income_base = 80 + np.random.uniform(-20, 40)
            capital_gains_income = capital_gains_income_base * base_growth * seasonal_factor
            capital_gains_tax_rate = 15 + np.random.uniform(-1, 2)  # Around 15%
            capital_gains_tax = capital_gains_income * (capital_gains_tax_rate / 100)
            
            total_income_tax = salaried_tax + corporate_tax + business_tax + capital_gains_tax
            
            # ---------- OTHER TAX CATEGORIES ----------
            
            # Sales Tax (largest component)
            sales_tax = (400 + np.random.uniform(-50, 100)) * base_growth * seasonal_factor
            
            # Customs Duty
            customs_duty = (180 + np.random.uniform(-30, 60)) * base_growth * seasonal_factor
            
            # Federal Excise
            federal_excise = (120 + np.random.uniform(-20, 40)) * base_growth * seasonal_factor
            
            total_collection = total_income_tax + sales_tax + customs_duty + federal_excise
            
            # ---------- LAFFER CURVE DYNAMICS ----------
            
            # As tax rates increase, reported income growth slows (diminishing returns)
            laffer_effect = max(0.3, 1 - (year_idx * 0.08))
            reported_income = salaried_income * laffer_effect
            
            # Elasticity calculation (response of reported income to tax rate changes)
            if year_idx == 0:
                elasticity = 1.0  # Start at 1:1 ratio
            else:
                # Calculate elasticity based on previous year
                prev_data = [d for d in data if d['year_index'] == year_idx - 1 and d['quarter'] == quarter]
                if prev_data:
                    prev_income = prev_data[0]['salaried_reported_income_billion']
                    prev_rate = prev_data[0]['salaried_tax_rate_percent']
                    
                    income_change_pct = (reported_income - prev_income) / prev_income if prev_income > 0 else 0
                    rate_change_pct = (salaried_tax_rate - prev_rate) / prev_rate if prev_rate > 0 else 0
                    
                    elasticity = income_change_pct / rate_change_pct if rate_change_pct != 0 else 1.0
                    # Ensure elasticity is reasonable (0.3 to 1.5)
                    elasticity = max(0.3, min(1.5, elasticity))
                else:
                    elasticity = 1.0
            
            # Salaried class burden (share of total income tax)
            salaried_burden_pct = (salaried_tax / total_income_tax) * 100
            
            # Revenue efficiency
            avg_rate = (salaried_tax_rate + corporate_tax_rate + business_tax_rate) / 3
            revenue_efficiency = total_collection / avg_rate if avg_rate > 0 else 0
            
            # Create record for each month in the quarter
            for month in months_map[quarter]:
                record = {
                    'fiscal_year': year,
                    'year_index': year_idx,
                    'quarter': quarter,
                    'quarter_index': quarter_idx,
                    'month': month,
                    
                    # Total Collection
                    'total_collection_billion': round(total_collection, 2),
                    
                    # Main Tax Categories
                    'income_tax_billion': round(total_income_tax, 2),
                    'sales_tax_billion': round(sales_tax, 2),
                    'customs_duty_billion': round(customs_duty, 2),
                    'federal_excise_billion': round(federal_excise, 2),
                    
                    # Income Tax Breakdown
                    'salaried_tax_billion': round(salaried_tax, 2),
                    'corporate_tax_billion': round(corporate_tax, 2),
                    'business_tax_billion': round(business_tax, 2),
                    'capital_gains_tax_billion': round(capital_gains_tax, 2),
                    
                    # Income Sources
                    'salaried_income_billion': round(salaried_income, 2),
                    'corporate_income_billion': round(corporate_income, 2),
                    'business_income_billion': round(business_income, 2),
                    'capital_gains_income_billion': round(capital_gains_income, 2),
                    
                    # Tax Rates
                    'salaried_tax_rate_percent': round(salaried_tax_rate, 2),
                    'corporate_tax_rate_percent': round(corporate_tax_rate, 2),
                    'business_tax_rate_percent': round(business_tax_rate, 2),
                    'capital_gains_tax_rate_percent': round(capital_gains_tax_rate, 2),
                    
                    # Laffer Curve Metrics
                    'salaried_reported_income_billion': round(reported_income, 2),
                    'laffer_effect': round(laffer_effect, 3),
                    'elasticity': round(elasticity, 3),
                    
                    # Burden Analysis
                    'salaried_burden_percent': round(salaried_burden_pct, 2),
                    
                    # Efficiency
                    'revenue_efficiency': round(revenue_efficiency, 2)
                }
                
                data.append(record)
    
    return pd.DataFrame(data)

if __name__ == '__main__':
    # Generate the data
    print("Generating FBR tax collection dataset...")
    df = generate_fbr_tax_data()
    
    # Ensure directory exists
    output_dir = 'data/dummy'
    os.makedirs(output_dir, exist_ok=True)
    
    # Save to CSV
    output_file = os.path.join(output_dir, 'fbr_tax_data.csv')
    df.to_csv(output_file, index=False)
    print(f"✓ Generated {len(df)} records")
    print(f"✓ Saved to {output_file}")
    
    # Print summary statistics
    print("\n" + "="*60)
    print("DATASET SUMMARY")
    print("="*60)
    print(f"Fiscal Years: {df['fiscal_year'].unique().tolist()}")
    print(f"Total Records: {len(df)}")
    print(f"\nTotal FBR Collection Range: Rs {df['total_collection_billion'].min():.1f}B - Rs {df['total_collection_billion'].max():.1f}B")
    print(f"Salaried Tax Rate Range: {df['salaried_tax_rate_percent'].min():.1f}% - {df['salaried_tax_rate_percent'].max():.1f}%")
    print(f"Elasticity Range: {df['elasticity'].min():.2f} - {df['elasticity'].max():.2f}")
    print(f"Salaried Burden Range: {df['salaried_burden_percent'].min():.1f}% - {df['salaried_burden_percent'].max():.1f}%")
    
    # Show sample data
    print("\n" + "="*60)
    print("SAMPLE DATA (First 5 rows)")
    print("="*60)
    print(df.head().to_string())
    
    print("\n✓ Dataset generation complete!")
