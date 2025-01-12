# validate_csv.py

import pandas as pd
import os

def validate_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Valid CSV: {file_path}")
        print("Columns:", df.columns.tolist())
        print(df.head())
        print("\n")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

csv_files = [
    "data/esg_tasks.csv",
    "data/benchmark_data.csv",
    "data/public_data.csv",
    "data/risk_data.csv",
    "data/performance_data.csv",
    "data/regulations.csv",
    "data/projects.csv",
    "data/scenario_data.csv",
    "data/kpi_data.csv",
    "data/compliance_tracker.csv"
]

for csv in csv_files:
    if os.path.exists(csv):
        validate_csv(csv)
    else:
        print(f"File not found: {csv}\n")