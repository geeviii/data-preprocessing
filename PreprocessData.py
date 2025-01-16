import pandas as pd

# Define column names
columns = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login",
    "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate",
    "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"
]

# get input and output file paths
input_file_path = input("Enter the path to the input dataset file (e.g., KDDTrain+.txt): ").strip()
output_file_path = input("Enter the path to save the cleaned dataset file (e.g., KDDTrain_Cleaned.csv): ").strip()

try:
    # Load and clean data
    train_data = pd.read_csv(input_file_path, header=None, names=columns)

    # Swap 'label' column with the 'dst_host_srv_rerror_rate' column
    train_data['label'], train_data['dst_host_srv_rerror_rate'] = train_data['dst_host_srv_rerror_rate'], train_data['label']

    # Re-encode labels to binary ('normal' or 'malicious')
    train_data['label'] = train_data['label'].apply(lambda x: 'malicious' if x != 'normal' else 'normal')

    # Save cleaned dataset
    train_data.to_csv(output_file_path, index=False)
    print(f"Cleaned dataset saved successfully to {output_file_path}.")

except FileNotFoundError:
    print(f"Error: File not found at {input_file_path}. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
