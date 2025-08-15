import pandas as pd
import os
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
from src.data.preprocess import preprocess_data
from src.utils.helpers import load_csv

MODEL_PATH = os.path.join("models", "trained_model.pkl")

def train_model(train_path):
    df = load_csv(train_path)
    df_processed = preprocess_data(df, target_col="Recycling Rate (%)", is_train=True)

    X = df_processed.drop(columns=["Recycling Rate (%)"])
    y = df_processed["Recycling Rate (%)"]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    param_grid = {"alpha": [0.001, 0.01, 0.1, 1, 10]}
    grid = GridSearchCV(Lasso(), param_grid, scoring="r2", cv=5)
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_
    y_pred = best_model.predict(X_val)

    print("Best Params:", grid.best_params_)
    print("R²:", r2_score(y_val, y_pred))
    print("MAE:", mean_absolute_error(y_val, y_pred))
    print("RMSE:", mean_squared_error(y_val, y_pred, squared=False))

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(best_model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_model("data/raw/train.csv")
