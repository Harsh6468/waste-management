import pandas as pd
import os
import joblib
from ..data.preprocess import preprocess_data
from ..utils.helpers import load_csv

MODEL_PATH = os.path.join("models", "final_model.pkl")

def make_predictions(test_path, output_path="predictions.csv"):
    df_test = load_csv(test_path)
    df_processed = preprocess_data(df_test)

    model = joblib.load(MODEL_PATH)
    preds = model.predict(df_processed)

    submission = pd.DataFrame({
        "ID": range(1, len(preds) + 1),
        "Recycling Rate (%)": preds
    })
    submission.to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")

if __name__ == "__main__":
    make_predictions("data/raw/test.csv")
