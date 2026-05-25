import pandas as pd
import os

def load_insurance_data(file_path=None):
    if file_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, "data", "insurance_data.csv")
    """
    Loads the insurance dataset and ensures basic structural parsing.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at: {file_path}. Please place it in your data/ folder.")
    
    # Load data
    df = pd.read_csv(file_path)
    
    # Pre-parse date/month dimensions if they exist
    if 'TransactionMonth' in df.columns:
        df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
        
    return df


