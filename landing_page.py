# pages/landing_page.py

import streamlit as st
import os

def display_landing_page():
    # Custom CSS for styling
    st.markdown("""
    <style>
    .title {
        font-size: 36px;
        color: #1f77b4;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .header {
        font-size: 24px;
        color: #ff7f0e;
        font-family: 'Arial', sans-serif;
    }
    .content {
        font-size: 18px;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Title
    st.markdown('<p class="title">Welcome to the Bank Leumi Environmental Compliance and Management Tool</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Define image path (absolute path based on project root)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    image_path = os.path.join(project_root, "assets", "decision_tool_workflow.png")
    
    # Display PNG image
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)  # Updated parameter
    else:
        st.warning("Decision tool workflow image not found in the assets folder.")
    
    st.markdown("---")
    
    # Information about Oporto Carbon
    st.markdown('<p class="header">About Oporto Carbon</p>', unsafe_allow_html=True)
    st.markdown('<p class="content">**Oporto Carbon** is a leading provider of sustainability and carbon management solutions. Their expertise and data resources are integral to the development and operation of this tool, ensuring accurate carbon pricing, offset credits, and compliance with regulatory frameworks.</p>', unsafe_allow_html=True)
    
    # Information about Dr. Avi Luvchik
    st.markdown('<p class="header">About Dr. Avi Luvchik</p>', unsafe_allow_html=True)
    st.markdown('<p class="content">**Dr. Avi Luvchik** is a renowned expert in environmental compliance and decision science. His leadership and expertise have been pivotal in designing the decision-making algorithms and ensuring the tool aligns with cutting-edge ESG (Environmental, Social, Governance) principles.</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.write("Please navigate through the sidebar to explore the tool's various features and modules.")