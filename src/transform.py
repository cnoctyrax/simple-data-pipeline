import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    # date -> echtes Datum
    df["date"] = pd.to_datetime(df["date"])

    # revenue berechnen
    df["revenue"] = df["quantity"] * df["price"]

    # saubere Spaltenreihenfolge
    df = df[["order_id", "date", "customer", "product", "quantity", "price", "revenue"]]

    return df

if __name__ == "__main__":
    df_raw = pd.read_csv("data/raw/sales.csv")
    df_clean = transform(df_raw)

    print("Transformed rows:", len(df_clean))
    print(df_clean.head())