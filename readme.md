# Data Engineering ETL Pipeline (v1)

Small ETL pipeline project to demonstrate data engineering fundamentals.

## What it does
- Extracts raw sales data from `data/raw/sales.csv`
- Transforms it (parses `date`, calculates `revenue = quantity * price`)
- Loads the cleaned dataset into `data/processed/sales_clean.csv`

## How to run
```bash
python src/extract.py
python src/transform.py
python src/load.py