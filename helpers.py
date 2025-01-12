# utils/helpers.py

import pandas as pd
import streamlit as st

# Define Color Variables
PRIMARY_COLOR = "#1f77b4"  # Replace with Bank Leumi’s primary color if different
SUCCESS_COLOR = "#2ca02c"
WARNING_COLOR = "#ff7f0e"
ERROR_COLOR = "#d62728"

def load_csv(file_path):
    """
    Loads a CSV file and returns a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded data/{file_path.split('/')[-1]} successfully.")
        return df
    except FileNotFoundError:
        print(f"File data/{file_path.split('/')[-1]} not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading data/{file_path.split('/')[-1]}: {e}")
        return pd.DataFrame()

def add_header(title):
    """
    Adds a consistent header to the page.
    """
    st.markdown(f"# {title}")
    st.markdown("---")

def add_footer():
    """
    Adds a consistent footer to the page.
    """
    st.markdown(
        """
        <hr>
        <div style="text-align: center; font-size: 12px; color: grey;">
            &copy; @all reserved rights. | Designed by Dr. Luvchik
        </div>
        """,
        unsafe_allow_html=True
    )

def calculate_financial_impact(df):
    """
    Calculates the financial impact based on Probability and Severity.
    """
    df['Financial_Impact'] = df['Probability'] * df['Severity']
    return df