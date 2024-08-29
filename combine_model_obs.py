import pandas as pd

def combine_datasets(file1, file2, output_file):
    # Read the first dataset (from the terminal output)
    df1 = pd.read_csv(file1)
    
    # Read the second dataset (with the 'STATION' column)
    df2 = pd.read_csv(file2)
    
    # Merge the two datasets on the 'TIME' column
    combined_df = pd.merge(df1, df2, on='DATETIME', how='outer')
    
    # Save the combined dataset to a new CSV file
    combined_df.to_csv(output_file, index=False)
    print(f"Combined dataset saved to {output_file}")

# Example usage
file1 = 'model_data.csv'  # The processed output from the first dataset
file2 = 'model_data_sekf.txt'  # The second dataset with the 'STATION' column
output_file = 'model_data_sekf.txt'  # The name of the output file

# Combine the datasets
combine_datasets(file1, file2, output_file)
