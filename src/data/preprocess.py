import pandas as pd
import numpy as np
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
import joblib
import os

ENCODERS_PATH = os.path.join("models", "encoders.pkl")

def preprocess_data(df: pd.DataFrame, target_col=None, is_train=True):
    encoders = joblib.load(ENCODERS_PATH)

    print(df['Waste Type'].values)
    print(df['Disposal Method'].values)
    for col in encoders["feature_names"]:
        if df['Disposal Method'].values[0] in col or df['Waste Type'].values[0] in col:
            df[col] = 1
        elif col not in df.columns:
            df[col] = 0
        
    categorical_low = ['Waste Type', 'Disposal Method']
    categorical_high = ['City/District']
    numerical_cols = [
        'Waste Generated (Tons/Day)', 'Population Density (People/km²)',
        'Municipal Efficiency Score (1-10)', 'Cost of Waste Management (₹/Ton)',
        'Awareness Campaigns Count', 'Landfill Capacity (Tons)', 'Year'
    ]

    df[categorical_high] = encoders["target_enc"].transform(df[categorical_high])

    # One-hot encode
    # df = pd.get_dummies(df, columns=categorical_low, drop_first=True)

    # Scale numerical
    df[numerical_cols] = encoders["scaler"].transform(df[numerical_cols])

    # Ensure same columns as training
    # for col in encoders["feature_names"]:
    #     if col not in df.columns:
    #         df[col] = 0
    df = df[encoders["feature_names"]]
    print(df.columns.tolist())
    print(df.iloc[0].tolist())
    return df
