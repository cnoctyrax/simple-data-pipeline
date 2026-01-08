from __future__ import annotations
import pandas as pd

def transform(
    df: pd.DataFrame,
    drop_duplicates: bool = True,
    drop_null_rows: bool = True
) -> pd.DataFrame:

    out = df.copy()

    # normalize column names
    out.columns = [c.strip().lower().replace(" ", "_") for c in out.columns]

    if drop_null_rows:
        out = out.dropna()

    if drop_duplicates:
        out = out.drop_duplicates()

    return out
