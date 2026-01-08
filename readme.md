# Data Engineering ETL Pipeline

Small end-to-end ETL pipeline project to demonstrate core data engineering fundamentals.

## What this project does
- Extracts raw sales data from a CSV file
- Cleans and standardizes the data
- Removes duplicate and null rows
- Saves a cleaned CSV snapshot
- Loads the data into a SQLite database

## Tech stack
- Python
- Pandas
- SQLite
- YAML configuration
- Logging

## Project structure
simple-data-pipeline/
├─ config/
│ └─ config.yaml
├─ data/
│ ├─ raw/
│ │ └─ sales.csv
│ └─ processed/
│ ├─ processed.csv
│ └─ pipeline.db
├─ logs/
├─ src/
│ ├─ extract.py
│ ├─ transform.py
│ ├─ load.py
│ ├─ pipeline.py
│ └─ utils.py
└─ README.md

## How to run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.pipeline --config config/config.yaml

