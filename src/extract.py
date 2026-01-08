from __future__ import annotations
import pandas as pd

def extract_csv(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path)
