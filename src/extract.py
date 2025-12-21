import pandas as pd

def extract_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print("Extracted rows:", len(df))
    print(df.head())
    return df

if __name__ == "__main__":
    extract_data("data/raw/sales.csv")