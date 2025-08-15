import pandas as pd
import numpy as np
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
import joblib
import os

ENCODERS_PATH = os.path.join("models", "encoders.pkl")

def preprocess_data(df, target_col=None, is_train=True):
    # Extract lat/lon
    if 'Landfill Location (Lat, Long)' in df.columns:
        df[['Landfill Lat', 'Landfill Lon']] = df['Landfill Location (Lat, Long)'] \
            .str.strip("()").str.split(",", expand=True).astype(float)
        df.drop(columns=['Landfill Location (Lat, Long)'], inplace=True)

    # Drop unnecessary columns
    if 'Landfill Name' in df.columns:
        df.drop(columns=['Landfill Name'], inplace=True)

    categorical_low = ['Waste Type', 'Disposal Method']
    categorical_high = ['City/District']
    numerical_cols = [
        'Waste Generated (Tons/Day)', 'Population Density (People/km²)',
        'Municipal Efficiency Score (1-10)', 'Cost of Waste Management (₹/Ton)',
        'Awareness Campaigns Count', 'Landfill Capacity (Tons)', 'Year',
        'Landfill Lat', 'Landfill Lon'
    ]

    df.fillna(df.mean(numeric_only=True), inplace=True)

    if is_train:
        target_enc = TargetEncoder(cols=categorical_high)
        df[categorical_high] = target_enc.fit_transform(df[categorical_high], df[target_col])

        scaler = StandardScaler()
        df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

        os.makedirs(os.path.dirname(ENCODERS_PATH), exist_ok=True)
        joblib.dump({"target_enc": target_enc, "scaler": scaler}, ENCODERS_PATH)
    else:
        encoders = joblib.load(ENCODERS_PATH)
        df[categorical_high] = encoders["target_enc"].transform(df[categorical_high])
        df[numerical_cols] = encoders["scaler"].transform(df[numerical_cols])

    df = pd.get_dummies(df, columns=categorical_low, drop_first=True)
    return df
