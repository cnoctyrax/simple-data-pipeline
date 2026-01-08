from __future__ import annotations
import argparse
import yaml
from pathlib import Path

from src.utils import ensure_dir, setup_logger
from src.extract import extract_csv
from src.transform import transform
from src.load import load_sqlite

def run(config_path: str) -> None:
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    ensure_dir(cfg["paths"]["raw_dir"])
    ensure_dir(cfg["paths"]["processed_dir"])

    logger = setup_logger(cfg["paths"]["logs_dir"])
    logger.info("Pipeline started")

    # EXTRACT
    df_raw = extract_csv(cfg["source"]["csv_path"])
    logger.info(f"Extracted {len(df_raw)} rows")

    # TRANSFORM
    df_clean = transform(
        df_raw,
        drop_duplicates=cfg["transform"]["drop_duplicates"],
        drop_null_rows=cfg["transform"]["drop_null_rows"]
    )
    logger.info(f"Transformed to {len(df_clean)} rows")

    # SAVE SNAPSHOT
    snapshot = Path(cfg["paths"]["processed_dir"]) / "processed.csv"
    df_clean.to_csv(snapshot, index=False)

    # LOAD
    inserted = load_sqlite(
        df_clean,
        cfg["load"]["sqlite_path"],
        cfg["load"]["table_name"]
    )

    logger.info(f"Loaded {inserted} rows into database")
    logger.info("Pipeline finished")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    run(args.config)
