#!/usr/bin/env python3
# %%
"""
Script to randomly sample 1000 rows from the dummy data CSV file
while maintaining uniform distribution across months and Union Councils (UCs).
"""

import pandas as pd
import numpy as np
from pathlib import Path

def sample_data_uniform(input_file, output_file, target_rows=1000):
    """
    Sample data to maintain uniform distribution across months and UCs.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
        target_rows (int): Target number of rows to keep (default: 1000)
    """
    
    # Read the CSV file
    print(f"Reading data from {input_file}...")
    df = pd.read_csv(input_file)
    
    print(f"Original dataset has {len(df)} rows")
    
    # Get unique values for stratification
    unique_months = df['month'].unique()
    unique_ucs = df['uc'].unique()
    
    print(f"Found {len(unique_months)} unique months: {sorted(unique_months)}")
    print(f"Found {len(unique_ucs)} unique UCs")
    
    # Calculate how many rows we want per month-UC combination
    total_combinations = len(unique_months) * len(unique_ucs)
    
    # Check if we have enough combinations for uniform distribution
    if total_combinations > target_rows:
        # If more combinations than target rows, sample 1 row per combination randomly
        print(f"Too many combinations ({total_combinations}) for {target_rows} target rows.")
        print("Randomly selecting month-UC combinations...")
        
        # Create all possible month-UC combinations
        combinations = []
        for month in unique_months:
            for uc in unique_ucs:
                combinations.append((month, uc))
        
        # Randomly select target_rows combinations
        selected_combinations = np.random.choice(
            len(combinations), 
            size=target_rows, 
            replace=False
        )
        
        sampled_data = []
        for idx in selected_combinations:
            month, uc = combinations[idx]
            # Get all rows for this month-UC combination
            subset = df[(df['month'] == month) & (df['uc'] == uc)]
            if not subset.empty:
                # Randomly select one row from this subset
                sampled_row = subset.sample(n=1)
                sampled_data.append(sampled_row)
        
        # Combine all sampled rows
        if sampled_data:
            result_df = pd.concat(sampled_data, ignore_index=True)
        else:
            result_df = pd.DataFrame()
            
    else:
        # If fewer combinations than target rows, sample multiple rows per combination
        rows_per_combination = target_rows // total_combinations
        extra_rows = target_rows % total_combinations
        
        print(f"Sampling {rows_per_combination} rows per month-UC combination...")
        print(f"Plus {extra_rows} additional rows distributed randomly")
        
        sampled_data = []
        extra_combinations = []
        
        # Sample base number of rows for each combination
        for month in unique_months:
            for uc in unique_ucs:
                subset = df[(df['month'] == month) & (df['uc'] == uc)]
                if not subset.empty:
                    # Sample rows_per_combination rows (or all if fewer available)
                    n_sample = min(rows_per_combination, len(subset))
                    if n_sample > 0:
                        sampled_rows = subset.sample(n=n_sample)
                        sampled_data.append(sampled_rows)
                        
                        # Track combinations that have data for extra sampling
                        if len(subset) > rows_per_combination:
                            extra_combinations.append((month, uc))
        
        # Sample additional rows to reach target
        if extra_rows > 0 and extra_combinations:
            print(f"Sampling {extra_rows} additional rows...")
            selected_extra = np.random.choice(
                len(extra_combinations), 
                size=min(extra_rows, len(extra_combinations)), 
                replace=False
            )
            
            for idx in selected_extra:
                month, uc = extra_combinations[idx]
                subset = df[(df['month'] == month) & (df['uc'] == uc)]
                # Exclude already sampled rows
                remaining_subset = subset[~subset.index.isin(
                    pd.concat(sampled_data).index if sampled_data else pd.DataFrame().index
                )]
                if not remaining_subset.empty:
                    extra_row = remaining_subset.sample(n=1)
                    sampled_data.append(extra_row)
        
        # Combine all sampled rows
        if sampled_data:
            result_df = pd.concat(sampled_data, ignore_index=True)
        else:
            result_df = pd.DataFrame()
    
    # Shuffle the final dataset
    result_df = result_df.sample(frac=1).reset_index(drop=True)
    
    print(f"\nFinal sampled dataset has {len(result_df)} rows")
    
    # Check distribution
    if not result_df.empty:
        print("\nDistribution by month:")
        month_dist = result_df['month'].value_counts().sort_index()
        print(month_dist)
        
        print(f"\nDistribution by UC (showing top 10):")
        uc_dist = result_df['uc'].value_counts()
        print(uc_dist.head(10))
        
        print(f"\nUnique months in sample: {len(result_df['month'].unique())}")
        print(f"Unique UCs in sample: {len(result_df['uc'].unique())}")
    
    # Save to file
    print(f"\nSaving sampled data to {output_file}...")
    result_df.to_csv(output_file, index=False)
    print("Done!")
    
    return result_df

def main():
    """Main function to execute the sampling."""
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Define file paths
    input_file = "data/dummy/dummy_data.csv"
    output_file = "data/dummy/dummy_data_sampled.csv"
    
    # Check if input file exists
    if not Path(input_file).exists():
        print(f"Error: Input file '{input_file}' not found!")
        print("Please make sure you're running this script from the correct directory.")
        return
    
    # Create output directory if it doesn't exist
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Sample the data
    try:
        sampled_df = sample_data_uniform(input_file, output_file, target_rows=1000)
        
        if len(sampled_df) > 0:
            print(f"\n✅ Successfully created sampled dataset with {len(sampled_df)} rows!")
            print(f"📁 Output saved to: {output_file}")
        else:
            print("❌ No data was sampled. Please check your input data.")
            
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
