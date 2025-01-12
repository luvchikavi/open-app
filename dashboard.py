# pages/dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import load_csv, add_header, add_footer

def display_esg_tasks():
    st.subheader("ESG Report Task List")
    esg_df = load_csv("data/esg_tasks.csv")
    if not esg_df.empty:
        # Display DataFrame
        st.dataframe(esg_df)
        
        # Download ESG Tasks
        csv = esg_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download ESG Tasks",
            data=csv,
            file_name='esg_tasks.csv',
            mime='text/csv',
            key='download_esg_tasks_unique'
        )
        
        # Optional: Group tasks by Responsible Department
        st.markdown("### Tasks by Department")
        grouped = esg_df.groupby('Responsible').size().reset_index(name='Task Count')
        fig = px.bar(
            grouped,
            x='Responsible',
            y='Task Count',
            title='Number of Tasks per Department',
            labels={'Responsible': 'Department', 'Task Count': 'Number of Tasks'},
            color='Responsible'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No ESG tasks available.")

def display_public_data_main():
    st.subheader("Public Data: Carbon Price, Tax, and Offset Credits")
    public_data = load_csv("data/public_data.csv")
    
    if not public_data.empty:
        # Display table
        st.dataframe(public_data)
        
        # Display chart
        fig = px.bar(
            public_data, 
            x='Country', 
            y=['Carbon_Price_USD_per_ton', 'Carbon_Tax_USD_per_ton', 'Carbon_Offset_Credits_USD_per_ton'],
            barmode='group',
            title='Carbon Price, Tax, and Offset Credits Comparison',
            labels={'value': 'USD per Ton', 'variable': 'Type'}
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Download Public Data
        csv = public_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Public Data",
            data=csv,
            file_name='public_data.csv',
            mime='text/csv',
            key='download_public_data_dashboard_unique'
        )
        
        # Download Chart as Image
        img_bytes = fig.to_image(format="png")
        st.download_button(
            label="Download Public Data Chart",
            data=img_bytes,
            file_name='public_data_chart.png',
            mime='image/png',
            key='download_public_data_chart_dashboard_unique'
        )
    else:
        st.warning("No public data available.")

def display_dashboard():
    add_header("Dashboard")
    display_esg_tasks()
    st.markdown("---")
    display_public_data_main()
    add_footer()

if __name__ == "__main__":
    display_dashboard()