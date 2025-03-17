import pandas as pd

def standardize_csv(filepath):
    """
    Standardizes a CSV file by removing the first part of strings in columns from the third column onwards.

    Args:
        filepath: The path to the CSV file.

    Returns:
        A pandas DataFrame with the standardized data.
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

    def extract_sample_id(string):
        """Extracts the sample ID after the comma and space."""
        try:
            return string.split(", ")[1]
        except (IndexError, AttributeError):
            return string

    for col in df.columns[2:]:
        df[col] = df[col].apply(extract_sample_id)

    # Correct Header
    header = list(df.columns)
    for i in range(2, len(header)):
        header[i] = extract_sample_id(header[i])
    df.columns = header

    return df

standardized_df = standardize_csv('no_head_corrected_fpkm.csv')

if standardized_df is not None:
    print(standardized_df.head()) #Print first few rows to confirm changes.

    # Save the standardized DataFrame to a new CSV file
    standardized_df.to_csv('standardized_file.csv', index=False)