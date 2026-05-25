import pandas as pd
import os

def clean_dataset():
    data_path = "data/insurance_data.csv"
    
    if not os.path.exists(data_path):
        print(f"Error: Could not find data file at {data_path}")
        return

    print("Loading raw data...")
    df = pd.read_csv(data_path)

    print("Cleaning column whitespaces and formatting dates...")
    df.columns = df.columns.str.strip()  # Clean up whitespace
    
    if 'TransactionMonth' in df.columns:
        df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])

    # Overwrite the file to update it
    df.to_csv(data_path, index=False)
    print("Data cleaning complete and saved! Ready to version with DVC.")

if __name__ == "__main__":
    clean_dataset()