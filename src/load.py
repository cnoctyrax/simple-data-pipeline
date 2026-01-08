from __future__ import annotations
import sqlite3
import pandas as pd
from pathlib import Path

def load_sqlite(df: pd.DataFrame, sqlite_path: str, table_name: str) -> int:
    Path(sqlite_path).parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(sqlite_path) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    return len(df)
