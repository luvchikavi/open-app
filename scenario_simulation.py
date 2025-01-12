# pages/scenario_simulation.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import load_csv, add_header, add_footer

def display_scenario_simulation():
    """
    Displays the Scenario Simulation page with scenarios and visualizations.
    """
    # Add Header
    add_header("Scenario Simulation")
    
    # Main Header
    st.header("Scenario Simulation Tool")
    
    # Load scenario data
    scenario_df = load_csv("data/scenario_data.csv")
    
    if not scenario_df.empty:
        # Display Scenarios Table
        st.subheader("Scenarios Overview")
        st.dataframe(scenario_df)
        
        # Download Scenario Data
        csv = scenario_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Scenario Data",
            data=csv,
            file_name='scenario_data.csv',
            mime='text/csv',
            key='download_scenario_data_unique'
        )
        
        # Scenario Selection
        st.subheader("Select a Scenario to Simulate")
        selected_scenario = st.selectbox("Choose Scenario", scenario_df['Scenario'])
        
        # Fetch Selected Scenario Details
        scenario_details = scenario_df[scenario_df['Scenario'] == selected_scenario].iloc[0]
        
        st.markdown(f"**Description:** {scenario_details['Description']}")
        st.markdown(f"**Investment:** ${scenario_details['Investment_USD']:,}")
        
        # Ensure 'Estimated_Carbon_Reduction_tons' is numeric
        try:
            carbon_reduction = float(scenario_details['Estimated_Carbon_Reduction_tons'])
            st.markdown(f"**Estimated Carbon Reduction:** {carbon_reduction:,.0f} tons")
        except ValueError:
            st.markdown("**Estimated Carbon Reduction:** Data not available")
        
        st.markdown(f"**Timeframe:** {scenario_details['Estimated_Timeframe']}")
        st.markdown(f"**Status:** {scenario_details['Status']}")
        
        # Ensure 'Estimated_Carbon_Reduction_tons' and 'Investment_USD' are numeric for plotting
        scenario_df['Estimated_Carbon_Reduction_tons'] = pd.to_numeric(scenario_df['Estimated_Carbon_Reduction_tons'], errors='coerce')
        scenario_df['Investment_USD'] = pd.to_numeric(scenario_df['Investment_USD'], errors='coerce')
        
        # Remove rows with NaN in critical columns
        scenario_df = scenario_df.dropna(subset=['Estimated_Carbon_Reduction_tons', 'Investment_USD'])
        
        # Visualization: Investment vs. Carbon Reduction
        st.subheader("Investment vs. Carbon Reduction")
        fig = px.scatter(
            scenario_df,
            x='Investment_USD',
            y='Estimated_Carbon_Reduction_tons',
            size='Estimated_Carbon_Reduction_tons',
            color='Status',
            hover_name='Scenario',
            title='Investment vs. Carbon Reduction Across Scenarios',
            labels={
                'Investment_USD': 'Investment (USD)',
                'Estimated_Carbon_Reduction_tons': 'Estimated Carbon Reduction (tons)'
            },
            size_max=60
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Download Chart as Image
        img_bytes = fig.to_image(format="png")
        st.download_button(
            label="Download Scenario Chart",
            data=img_bytes,
            file_name='scenario_chart.png',
            mime='image/png',
            key='download_scenario_chart_unique'
        )
        
    else:
        st.warning("No scenario data available.")
    
    # Add Footer
    add_footer()

def display_scenario_simulation_page():
    """
    Wrapper function to display the Scenario Simulation page.
    """
    display_scenario_simulation()

if __name__ == "__main__":
    display_scenario_simulation_page()