import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def preprocess_insurance_data(df):
    """
    Handles missing values, engineers core features, and encodes categories.
    """
    df_clean = df.copy()
    
    # 1. Feature Engineering
    # Calculate vehicle age relative to the data period (approx 2015)
    if 'RegistrationYear' in df_clean.columns:
        df_clean['VehicleAge'] = 2015 - df_clean['RegistrationYear']
    else:
        df_clean['VehicleAge'] = 0
        
    # 2. Basic Missing Value Imputation
    numerical_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        
    categorical_cols = df_clean.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df_clean[col] = df_clean[col].fillna('Unknown')
        
    # 3. Select important tracking features to avoid huge sparse matrices
    keep_features = ['VehicleAge', 'CustomValueEstimate', 'Cylinders', 'Cubiccapacity', 
                     'Gender', 'Province', 'CoverCategory', 'VehicleType']
    
    # Filter down to features that actually exist in your dataset
    existing_features = [f for f in keep_features if f in df_clean.columns]
    
    # One-Hot Encoding for categorical features
    X = pd.get_dummies(df_clean[existing_features], drop_first=True)
    
    return X, df_clean

def evaluate_regression(y_true, y_pred):
    """
    Returns standard regression valuation parameters.
    """
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return rmse, r2