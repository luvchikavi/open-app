# pages/analysis.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import load_csv, add_header, add_footer, calculate_financial_impact, SUCCESS_COLOR, WARNING_COLOR, ERROR_COLOR

def display_climate_risk():
    """
    Displays the Climate Risk Analysis page with risk data and visualizations.
    """
    # Add Header
    add_header("Climate Risk Analysis")
    
    # Main Header
    st.header("Climate Risk Assessment")
    
    # Load risk data
    risk_df = load_csv("data/risk_data.csv")
    
    if not risk_df.empty:
        # Calculate financial impact
        risk_df = calculate_financial_impact(risk_df)
        
        # Display risk data
        st.subheader("Risk Data")
        st.dataframe(risk_df)
        
        # Download Risk Data
        csv = risk_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Risk Data",
            data=csv,
            file_name='risk_data.csv',
            mime='text/csv',
            key='download_risk_data_unique'
        )
        
        # Visualization: Financial Impact by Risk Subcategory
        st.subheader("Financial Impact by Risk Subcategory")
        fig = px.bar(
            risk_df, 
            x='Subcategory', 
            y='Financial_Impact',
            color='Risk_Category',
            title='Financial Impact by Risk Subcategory',
            labels={'Financial_Impact': 'Financial Impact (USD)'}
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Total Financial Impact
        st.subheader("Total Financial Impact")
        total_impact = risk_df['Financial_Impact'].sum()
        
        # Display Total Financial Impact
        st.write(f"**Total Financial Impact:** ${total_impact:,.2f}")
        
        # Interactive Slider: Adjust Severity of Each Risk
        st.subheader("Adjust Risk Severity to Explore Financial Impact")
        adjusted_severity = risk_df.copy()
        for index, row in adjusted_severity.iterrows():
            adjusted_severity.at[index, 'Severity'] = st.slider(
                label=f"Adjust Severity for {row['Subcategory']}",
                min_value=0,
                max_value=int(row['Severity'] * 2),  # Allow up to double the severity
                value=int(row['Severity']),
                step=100000,
                key=f"severity_slider_{index}"
            )
        
        # Recalculate Financial Impact based on adjusted severity
        adjusted_severity['Financial_Impact'] = adjusted_severity['Probability'] * adjusted_severity['Severity']
        adjusted_total_impact = adjusted_severity['Financial_Impact'].sum()
        
        # Display Adjusted Total Financial Impact
        st.write(f"**Adjusted Total Financial Impact:** ${adjusted_total_impact:,.2f}")
        
        # Visualization: Adjusted Financial Impact
        st.subheader("Adjusted Financial Impact by Risk Subcategory")
        fig_adjusted = px.bar(
            adjusted_severity, 
            x='Subcategory', 
            y='Financial_Impact',
            color='Risk_Category',
            title='Adjusted Financial Impact by Risk Subcategory',
            labels={'Financial_Impact': 'Financial Impact (USD)'}
        )
        st.plotly_chart(fig_adjusted, use_container_width=True)
        
        # Download Adjusted Risk Data
        csv_adjusted = adjusted_severity.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Adjusted Risk Data",
            data=csv_adjusted,
            file_name='adjusted_risk_data.csv',
            mime='text/csv',
            key='download_adjusted_risk_data_unique'
        )
        
        # Summary Metrics
        st.subheader("Summary")
        st.write(f"**Total Financial Impact:** ${total_impact:,.2f}")
        st.write(f"**Adjusted Total Financial Impact:** ${adjusted_total_impact:,.2f}")
        
        # Download Summary as Text
        summary_text = f"Total Financial Impact: ${total_impact:,.2f}\nAdjusted Total Financial Impact: ${adjusted_total_impact:,.2f}"
        st.download_button(
            label="Download Summary",
            data=summary_text,
            file_name='summary.txt',
            mime='text/plain',
            key='download_summary_unique'
        )
    else:
        st.warning("No climate risk data available.")
    
    # Add Footer
    add_footer()

def display_climate_risk_page():
    """
    Wrapper function to display the Climate Risk Analysis page.
    """
    display_climate_risk()

if __name__ == "__main__":
    display_climate_risk_page()