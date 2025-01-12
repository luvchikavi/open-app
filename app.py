import streamlit as st
from PIL import Image
import importlib
import os

# Set page configuration
st.set_page_config(page_title="Bank Leumi Environmental Tool", layout="wide")

# Load logos
col1, col2 = st.columns([1, 1])
with col1:
    logo_path = "assets/client_logo.png"
    if os.path.exists(logo_path):
        client_logo = Image.open(logo_path)
        st.image(client_logo, width=150)
    else:
        st.warning("Client logo not found.")
with col2:
    logo_path = "assets/oporto_logo.png"
    if os.path.exists(logo_path):
        oporto_logo = Image.open(logo_path)
        st.image(oporto_logo, width=150)
    else:
        st.warning("Oporto logo not found.")

st.title("Bank Leumi Environmental Compliance and Management Tool")
st.markdown("---")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", [
    "Landing Page",         # Added Landing Page as the first option
    "Dashboard",
    "Climate Risk Analysis",
    "Regulations",
    "Project Prioritization",
    "KPI Dashboard",
    "Scenario Simulation",
    "Compliance Tracker",
    "Task Tracker"          # Include if task_tracker.py is implemented
])

# Page Navigation
if page == "Landing Page":
    landing_page = importlib.import_module("pages.landing_page")
    landing_page.display_landing_page()
elif page == "Dashboard":
    dashboard = importlib.import_module("pages.dashboard")
    dashboard.display_dashboard()
elif page == "Climate Risk Analysis":
    climate_risk = importlib.import_module("pages.analysis")
    climate_risk.display_climate_risk()
elif page == "Regulations":
    regulations = importlib.import_module("pages.regulations")
    regulations.display_regulations()
elif page == "Project Prioritization":
    project_prioritization = importlib.import_module("pages.project_prioritization")
    project_prioritization.display_project_prioritization()
elif page == "KPI Dashboard":
    kpi_dashboard = importlib.import_module("pages.kpi_dashboard")
    kpi_dashboard.display_kpi_dashboard()
elif page == "Scenario Simulation":
    scenario_simulation = importlib.import_module("pages.scenario_simulation")
    scenario_simulation.display_scenario_simulation()
elif page == "Compliance Tracker":
    compliance_tracker = importlib.import_module("pages.compliance_tracker")
    compliance_tracker.display_compliance_tracker_page()
elif page == "Task Tracker":
    task_tracker = importlib.import_module("pages.task_tracker")
    task_tracker.display_task_tracker_page()

# Print Instructions
st.sidebar.markdown("---")
st.sidebar.header("Print Dashboard")
st.sidebar.info(
    "To print the dashboard, use your browser's print functionality. "
    "Press `Ctrl + P` (Windows) or `Cmd + P` (Mac) and select the desired print options."
)