import pandas as pd

def load_csv(path):
    """Loads a CSV file into a DataFrame."""
    return pd.read_csv(path)
