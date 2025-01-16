import pandas as pd

# get input and output file paths
input_file_path = input("Enter the path to the correlation matrix file (e.g., matrix.csv): ").strip()
output_file_path = input("Enter the path to save the reshaped matrix file (e.g., reshaped.csv): ").strip()

# Load the correlation matrix
correlation_matrix = pd.read_csv(input_file_path, index_col=0)

# Reshape the matrix into long form
correlation_long = correlation_matrix.stack().reset_index()
correlation_long.columns = ['Feature1', 'Feature2', 'Correlation']

# Save reshaped data
correlation_long.to_csv(output_file_path, index=False)