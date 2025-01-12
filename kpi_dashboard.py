# pages/kpi_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import load_csv, add_header, add_footer

def display_kpi_dashboard():
    """
    Displays the KPI Dashboard with Metrics Overview and Progress Overview.
    """
    # Add Header
    add_header("KPI Dashboard")
    
    # Main Header
    st.header("Key Performance Indicators (KPIs)")

    # Load KPI data
    kpi_df = load_csv("data/kpi_data.csv")

    if not kpi_df.empty:
        # Define Colors
        PRIMARY_COLOR = "#1f77b4"  # Replace with Bank Leumi’s primary color if different
        SUCCESS_COLOR = "#2ca02c"
        WARNING_COLOR = "#ff7f0e"
        ERROR_COLOR = "#d62728"

        # --- KPI Metrics Overview ---
        st.subheader("KPI Metrics Overview")
        num_kpis = len(kpi_df)
        
        # Create columns for displaying KPI metrics
        cols = st.columns(3)  # Adjust number of columns based on the number of KPIs

        for index, row in kpi_df.iterrows():
            kpi = row['KPI']
            value = row['Value']
            target = row['Target']
            status = row['Status']

            # Convert 'Value' and 'Target' to float for calculations
            try:
                value_numeric = float(value)
            except ValueError:
                value_numeric = 0  # Default to 0 if conversion fails

            try:
                target_numeric = float(target)
            except ValueError:
                target_numeric = 1  # Avoid division by zero

            # Assign each KPI to a column to prevent overlap
            col = cols[index % 3]
            with col:
                # Calculate percentage towards target
                try:
                    percentage = (value_numeric / target_numeric) * 100
                except ZeroDivisionError:
                    percentage = 0

                # Define delta color and status color based on KPI status
                if status == "On Track":
                    delta_color = "normal"
                    status_color = "green"
                elif status == "Off Track":
                    delta_color = "inverse"
                    status_color = "red"
                elif status == "Under Target":
                    delta_color = "normal"
                    status_color = "orange"
                else:
                    delta_color = "normal"
                    status_color = "blue"  # Default color

                # Display the KPI metric
                st.metric(
                    label=kpi,
                    value=f"${value_numeric:,.0f}",
                    delta=f"{percentage:.1f}% towards target",
                    delta_color=delta_color
                )
                # Display the status with a colored dot
                st.markdown(f'<span style="color:{status_color};">●</span> {status}', unsafe_allow_html=True)

        # --- KPI Progress Overview ---
        st.subheader("KPI Progress Overview")

        # Prepare data for the grouped bar chart
        kpi_melted = kpi_df.melt(
            id_vars=['KPI'],
            value_vars=['Value', 'Target'],
            var_name='Type',
            value_name='Amount'
        )
        kpi_melted['Amount'] = pd.to_numeric(kpi_melted['Amount'], errors='coerce')
        kpi_melted = kpi_melted.dropna(subset=['Amount'])  # Remove rows with NaN values

        # Create a grouped bar chart comparing current values against targets
        fig = px.bar(
            kpi_melted,
            x='KPI',
            y='Amount',
            color='Type',
            barmode='group',
            title='Current Values vs. Targets',
            labels={'Amount': 'Amount (USD)', 'KPI': 'Key Performance Indicator'},
            color_discrete_map={'Value': PRIMARY_COLOR, 'Target': "lightgray"},
            text='Amount'
        )

        # Enhance the chart layout
        fig.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        fig.update_layout(
            uniformtext_minsize=8,
            uniformtext_mode='hide',
            xaxis_title="KPI",
            yaxis_title="Amount (USD)",
            legend_title="Type",
            title_x=0.5  # Center the title
        )

        # Display the grouped bar chart
        st.plotly_chart(fig, use_container_width=True)

        # --- Download KPI Data ---
        csv = kpi_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download KPI Data",
            data=csv,
            file_name='kpi_data.csv',
            mime='text/csv',
            key='download_kpi_data_unique'  # Ensure the key is unique
        )

        # Add Footer
        add_footer()
    else:
        st.warning("No KPI data available.")

def display_kpi_dashboard_page():
    """
    Wrapper function to display the KPI Dashboard page.
    """
    display_kpi_dashboard()

if __name__ == "__main__":
    display_kpi_dashboard_page()