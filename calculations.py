# utils/calculations.py

import pandas as pd

def calculate_financial_impact(df):
    """
    Calculate the financial impact based on probability and severity.
    Financial Impact = Probability * Severity
    """
    if 'Probability' in df.columns and 'Severity' in df.columns:
        df['Financial_Impact'] = df['Probability'] * df['Severity']
    else:
        print("Required columns 'Probability' or 'Severity' not found in DataFrame.")
        df['Financial_Impact'] = 0
    return df