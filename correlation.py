import pandas as pd

# get input and output file paths
input_file_path = input("Enter the path to the cleaned dataset file (e.g., KDDTrain_Cleaned.csv): ").strip()
output_file_path = input("Enter the path to save the correlation matrix file (e.g., matrix.csv): ").strip()

# Load the dataset
df = pd.read_csv(input_file_path)

# Select numerical columns for correlation
numerical_cols = ['count', 'serror_rate', 'srv_count']
correlation_matrix = df[numerical_cols].corr()

# Save the correlation matrix as a CSV for Tableau
correlation_matrix.to_csv(output_file_path, index=False)