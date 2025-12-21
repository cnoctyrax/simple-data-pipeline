import pandas as pd
from pathlib import Path

def load_to_csv(df: pd.DataFrame, output_path: str) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved file -> {output_path}")

if __name__ == "__main__":
    # raw einlesen
    df_raw = pd.read_csv("data/raw/sales.csv")

    # transform (minimal hier drin, später trennen wir das sauber)
    df_raw["date"] = pd.to_datetime(df_raw["date"])
    df_raw["revenue"] = df_raw["quantity"] * df_raw["price"]
    df_out = df_raw[["order_id", "date", "customer", "product", "quantity", "price", "revenue"]]

    # load
    load_to_csv(df_out, "data/processed/sales_clean.csv")
