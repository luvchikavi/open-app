# pages/compliance_tracker.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import load_csv, add_header, add_footer, SUCCESS_COLOR, WARNING_COLOR, ERROR_COLOR

def display_compliance_tracker():
    """
    Displays the Compliance Tracker page with compliance data and visualizations.
    """
    add_header("Compliance Tracker")
    
    st.header("Regulatory Compliance Status")
    
    # Load compliance data
    compliance_df = load_csv("data/compliance_tracker.csv")
    
    if not compliance_df.empty:
        # Display Compliance Data
        st.subheader("Compliance Status Table")
        st.dataframe(compliance_df)
        
        # Download Compliance Data
        csv = compliance_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Compliance Data",
            data=csv,
            file_name='compliance_tracker.csv',
            mime='text/csv',
            key='download_compliance_tracker_unique'
        )
        
        # Visualization: Compliance Status Pie Chart
        st.subheader("Compliance Status Distribution")
        fig = px.pie(
            compliance_df,
            names='Compliance_Status',
            title='Compliance Status Distribution',
            color='Compliance_Status',
            color_discrete_map={
                'Compliant': SUCCESS_COLOR,
                'In Progress': WARNING_COLOR,
                'Planned': ERROR_COLOR
            }
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Download Chart as Image
        img_bytes = fig.to_image(format="png")
        st.download_button(
            label="Download Compliance Chart",
            data=img_bytes,
            file_name='compliance_chart.png',
            mime='image/png',
            key='download_compliance_chart_unique'
        )
    else:
        st.warning("No compliance data available.")
    
    add_footer()

def display_compliance_tracker_page():
    """
    Wrapper function to display the Compliance Tracker page.
    """
    display_compliance_tracker()

if __name__ == "__main__":
    display_compliance_tracker_page()           