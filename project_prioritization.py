# pages/project_prioritization.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import load_csv, add_header, add_footer

def display_project_prioritization():
    add_header("Project Prioritization")
    
    st.header("Environmental Project Prioritization")
    
    # Load projects data
    projects_df = load_csv("data/projects.csv")
    
    if not projects_df.empty:
        # Display Projects Table
        st.subheader("Projects Overview")
        st.dataframe(projects_df)
        
        # Download Projects Data
        csv = projects_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Projects Data",
            data=csv,
            file_name='projects.csv',
            mime='text/csv',
            key='download_projects_data_unique'
        )
        
        # Scatter Plot: ROI vs. Carbon Reduction
        st.subheader("ROI vs. Carbon Reduction")
        fig = px.scatter(
            projects_df,
            x='Estimated_Carbon_Reduction_tons',
            y='ROI_Percentage',
            size='Estimated_Carbon_Reduction_tons',
            color='Department',
            hover_name='Project',
            title='ROI vs. Carbon Reduction',
            labels={
                'Estimated_Carbon_Reduction_tons': 'Estimated Carbon Reduction (tons)',
                'ROI_Percentage': 'Return on Investment (%)'
            },
            size_max=60
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Bar Chart: Priority Score by Project
        st.subheader("Priority Scores")
        fig_priority = px.bar(
            projects_df,
            x='Project',
            y='Priority_Score',
            color='Priority_Score',
            title='Project Priority Scores',
            labels={'Priority_Score': 'Priority Score'},
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_priority, use_container_width=True)
        
        # Map Visualization: Project Locations
        st.subheader("Project Locations Map")
        fig_map = px.scatter_mapbox(
            projects_df,
            lat="Latitude",
            lon="Longitude",
            hover_name="Project",
            hover_data=["Description", "Estimated_Carbon_Reduction_tons", "Department"],
            color="Department",
            size="Estimated_Carbon_Reduction_tons",
            size_max=15,
            zoom=10,
            height=600,
            title="Geographical Distribution of Projects"
        )
        fig_map.update_layout(mapbox_style="open-street-map")
        fig_map.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
        st.plotly_chart(fig_map, use_container_width=True)
        
        # Download Charts
        img_bytes_scatter = fig.to_image(format="png")
        st.download_button(
            label="Download ROI vs. Carbon Reduction Chart",
            data=img_bytes_scatter,
            file_name='roi_carbon_reduction_chart.png',
            mime='image/png',
            key='download_roi_carbon_chart_unique'
        )
        
        img_bytes_priority = fig_priority.to_image(format="png")
        st.download_button(
            label="Download Priority Scores Chart",
            data=img_bytes_priority,
            file_name='priority_scores_chart.png',
            mime='image/png',
            key='download_priority_scores_chart_unique'
        )
        
        img_bytes_map = fig_map.to_image(format="png")
        st.download_button(
            label="Download Project Locations Map",
            data=img_bytes_map,
            file_name='project_locations_map.png',
            mime='image/png',
            key='download_project_locations_map_unique'
        )
        
    else:
        st.warning("No projects data available.")
    
    add_footer()

def display_project_prioritization_page():
    display_project_prioritization()

if __name__ == "__main__":
    display_project_prioritization_page()