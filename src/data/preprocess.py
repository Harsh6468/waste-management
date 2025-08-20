import pandas as pd
import numpy as np
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
import joblib
import os

ENCODERS_PATH = os.path.join("models", "encoders.pkl")

def preprocess_data(df: pd.DataFrame, target_col=None, is_train=True):
    encoders = joblib.load(ENCODERS_PATH)
    
    df.drop(columns=['Landfill Name', 'Landfill Location (Lat, Long)'], errors="ignore", inplace=True)
        
    categorical_high = ['City/District']  # Target encoding
    categorical_low = ['Waste Type', 'Disposal Method']  # One-hot encoding
    numerical_cols = [
        'Waste Generated (Tons/Day)', 'Population Density (People/km²)',
        'Municipal Efficiency Score (1-10)', 'Cost of Waste Management (₹/Ton)',
        'Awareness Campaigns Count', 'Landfill Capacity (Tons)', 'Year'
    ]
    
    if is_train:
        target_enc = TargetEncoder(cols=categorical_high)
        df[categorical_high] = target_enc.fit_transform(df[categorical_high], df[target_col])

        # One-Hot Encoding for low-cardinality categorical features
        df = pd.get_dummies(df, columns=categorical_low, drop_first=True)

        # Standardize numerical features
        scaler = StandardScaler()
        df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
        
        final_columns = df.columns.to_list()
        final_columns.remove('Recycling Rate (%)')

        # Save encoders for inference
        joblib.dump({'target_enc': target_enc, 'scaler': scaler, "feature_names": final_columns}, ENCODERS_PATH)
    else:
        for col in encoders["feature_names"]:
            if df['Disposal Method'].values[0] in col or df['Waste Type'].values[0] in col:
                df[col] = 1
            elif col not in df.columns:
                df[col] = 0
        df[categorical_high] = encoders["target_enc"].transform(df[categorical_high])
        df[numerical_cols] = encoders["scaler"].transform(df[numerical_cols])

    df = df[encoders["feature_names"]]
    return df
