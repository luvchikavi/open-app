# pages/regulations.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import load_csv, add_header, add_footer, SUCCESS_COLOR, WARNING_COLOR, ERROR_COLOR

def display_regulations():
    """
    Displays the Regulations page with a table and visualization.
    """
    # Add Header
    add_header("Regulations")
    
    # Main Header
    st.header("Regulatory Compliance Overview")
    
    # Load regulations data
    regulations_df = load_csv("data/regulations.csv")
    
    if not regulations_df.empty:
        # Display Regulations Table
        st.subheader("Regulations Overview")
        st.dataframe(regulations_df)
        
        # Download Regulations Data
        csv = regulations_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Regulations Data",
            data=csv,
            file_name='regulations.csv',
            mime='text/csv',
            key='download_regulations_unique'
        )
        
        # Visualization: Regulations Status Pie Chart
        st.subheader("Regulations Status Distribution")
        fig = px.pie(
            regulations_df,
            names='Status',
            title='Regulations Status Distribution',
            color='Status',
            color_discrete_map={
                'Completed': SUCCESS_COLOR,
                'In Progress': WARNING_COLOR,
                'Planned': ERROR_COLOR
            }
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Download Chart as Image
        img_bytes = fig.to_image(format="png")
        st.download_button(
            label="Download Regulations Chart",
            data=img_bytes,
            file_name='regulations_chart.png',
            mime='image/png',
            key='download_regulations_chart_unique'
        )
    else:
        st.warning("No regulations data available.")
    
    # Add Footer
    add_footer()

def display_regulations_page():
    """
    Wrapper function to display the Regulations page.
    """
    display_regulations()

if __name__ == "__main__":
    display_regulations_page()