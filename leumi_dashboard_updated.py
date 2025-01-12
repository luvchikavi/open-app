# leumi_dashboard_updated.py

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os

# --- Debug prints to verify logo file existence ---
print(os.path.exists("/Users/aviluvchik/z_CLEARAPP/BankLeumi/bank_leumi_tool/assets/oporto_logo.png"))
print(os.path.exists("/Users/aviluvchik/z_CLEARAPP/BankLeumi/bank_leumi_tool/assets/leumi_logo.png"))

# --- Paths for logos ---
script_dir = os.path.dirname(__file__)  # Directory of the script
oporto_logo_path = os.path.join(script_dir, "assets", "oporto_logo.png")
leumi_logo_path = os.path.join(script_dir, "assets", "leumi_logo.png")  # Assuming 'leumi_logo.png' is Bank Leumi's logo

# --- Set up the page configuration ---
st.set_page_config(page_title="Bank Leumi ESG and Sustainability Dashboard", layout="wide")

# --- Remove extra space at the top for each page ---
st.markdown(
    """
    <style>
    /* Remove extra spacing at the top */
    .css-18e3th9 {
        padding-top: 1rem !important;
    }
    .css-h5rgaw {
        padding-top: 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Helper function to display both logos at the top of each tab ---
def display_logos():
    if not os.path.exists(oporto_logo_path) or not os.path.exists(leumi_logo_path):
        st.warning("Logos not found. Please check file paths.")
    else:
        col1, col2, col3 = st.columns([1, 5, 1])
        with col1:
            st.image(oporto_logo_path, width=200)
        with col3:
            st.image(leumi_logo_path, width=200)

# --- Reusable footer for each tab ---
def display_footer():
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <hr>
            <p>&copy; 2025 Oporto Carbon. All Rights Reserved. Developed by Dr. Avi Luvchik.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------- Sidebar Navigation -------------------------- #
tabs = [
    "Landing Page",
    "Portfolio Carbon Analysis",
    "Compliance & Regulatory",
    "Financial Analysis",
    "Decision Support Tools",
    "KPI Metrics Overview"  # Added KPI Metrics Overview
]
page = st.sidebar.radio("Navigate to:", tabs)

# ========================= 1) LANDING PAGE =========================
if page == "Landing Page":
    display_logos()

    st.title("Welcome to the Bank Leumi ESG and Sustainability Dashboard")
    st.subheader("Empowering Sustainable Finance and Decision-Making")

    st.header("About This Dashboard")
    st.write(
        "This high-end tool has been developed to provide Bank Leumi with insights into its ESG performance, "
        "compliance status, and climate risk assessment. The dashboard enables data-driven decision-making "
        "to meet sustainability goals and ensure compliance with global frameworks."
    )

    st.header("About Oporto Carbon")
    st.write(
        "Oporto Carbon specializes in sustainability consulting and carbon management solutions. "
        "With a proven track record of helping organizations achieve their ESG goals, Oporto Carbon is "
        "a trusted partner for businesses navigating the complexities of climate change and regulatory compliance."
    )

    # "About Dr. Avi Luvchik" in bold, but NOT as a header/subheader
    st.markdown("**About Dr. Avi Luvchik**")
    st.write(
        "Dr. Avi Luvchik is the founder and CEO of Oporto Carbon. With extensive experience in sustainability "
        "and emissions reduction strategies, Dr. Luvchik has been instrumental in developing innovative solutions "
        "for organizations worldwide. His leadership and expertise drive the success of Oporto Carbon's projects."
    )

    display_footer()

# ================== 2) PORTFOLIO CARBON ANALYSIS ==================
elif page == "Portfolio Carbon Analysis":
    display_logos()

    st.title("Portfolio Carbon Analysis")
    st.write("Analyze the carbon footprint of the bank's operations, investments, and lending portfolio.")

    # 2.1 Detailed Emissions Table
    st.header("Detailed Emissions Overview")
    emissions_data = pd.DataFrame({
        "Scope": [
            "Scope 1", "Scope 1", "Scope 2", "Scope 2", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3",
            "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3",
            "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3", "Scope 3"
        ],
        "Category": [
            "Direct Emissions - Office Energy Use", "Direct Emissions - Company Vehicles",
            "Indirect Energy Emissions - Purchased Electricity", "Indirect Energy Emissions - Cooling Systems",
            "Financed Emissions - Corporate Loans", "Financed Emissions - Investments", "Business Travel",
            "Supply Chain Emissions", "Data Centers", "Waste Management", "Office Supplies", "Outsourced Services",
            "IT Equipment", "Marketing Activities", "Logistics Services", "Capital Goods", "Professional Services",
            "Training Programs", "Food Services", "Printing Services", "Telecommunications", "Insurance Services",
            "Legal Services", "Banking Services", "Cleaning Services", "Temporary Staffing"
        ],
        "Emissions 2024 (tons CO₂)": [
            3049, 2542, 1698, 3958, 1975, 3799, 2892, 3956, 3294, 2239,
            4523, 3783, 556, 1688, 4327, 2853, 1442, 4102, 3541, 3150,
            3449, 4282, 4126, 1486, 2226, 3601
        ],
        "Target 2030 (tons CO₂)": [
            1328, 670, 729, 855, 1224, 1965, 1105, 1542, 1186, 1206,
            2320, 1550, 259, 949, 2316, 1362, 857, 1935, 1038, 747,
            207, 79, 819, 1068, 1458, 2746
        ],
        "% of Target": [
            0.5644, 0.7364, 0.5707, 0.7840, 0.3803, 0.4828, 0.6179, 0.6102, 0.6400, 0.4614,
            0.4871, 0.5903, 0.5342, 0.4378, 0.4648, 0.5226, 0.4057, 0.5283, 0.7069, 0.7629,
            0.9400, 0.9820, 0.8015, 0.2813, 0.3450, 0.2374
        ],
        "Owner": [
            "Finance", "Legal", "Finance", "Legal", "IT Department", "HR", "Legal", "Finance", "HR", "Finance",
            "Legal", "HR", "HR", "Sustainability Team", "Sustainability Team", "Operations", "Sustainability Team",
            "IT Department", "Sustainability Team", "Operations", "Sustainability Team", "HR", "Sustainability Team",
            "Operations", "Sustainability Team", "Finance"
        ]
    })
    st.dataframe(emissions_data)

    # 2.2 Comparison to Targets
    st.header("Progress Toward Targets")
    progress_chart = px.bar(
        emissions_data,
        x="Category",
        y=["Emissions 2024 (tons CO₂)", "Target 2030 (tons CO₂)"],
        title="Emissions vs. Targets",
        barmode="group",
        labels={"value": "Tons CO₂", "variable": "Type"},
        height=600
    )
    st.plotly_chart(progress_chart, use_container_width=True)

    # 2.3 Path to Net Zero
    st.header("Path to Net Zero")
    tasks = pd.DataFrame({
        "Task": [
            "Achieve zero deforestation in financed projects",
            "Engage 80% of staff in sustainability training",
            "Transition all data centers to renewable energy",
            "Expand green financing portfolio by 40%",
            "Implement supplier ESG audits for top 50 suppliers",
            "Achieve 25% waste reduction in operations",
            "Conduct water usage audits and reduce consumption by 20%",
            "Achieve 100% digital communication and reduce printing by 90%",
            "Replace 60% of company vehicles with electric vehicles",
            "Increase renewable energy usage to 50%",
            "Implement circular economy practices in office operations",
            "Offset 100% of unavoidable emissions through verified carbon offsets",
            "Retrofit all office buildings for energy efficiency"
        ],
        "Deadline": pd.date_range(start="2023-01-01", periods=13, freq="2A").strftime("%Y-%m-%d"),
        "Completion (%)": [20, 45, 15, 35, 50, 30, 25, 80, 10, 40, 20, 5, 15],
        "Owner": [
            "Finance", "HR", "IT Department", "Sustainability Team", "Sustainability Team", "Operations", "Finance",
            "IT Department", "Operations", "Sustainability Team", "HR", "Legal", "Sustainability Team"
        ]
    })
    st.subheader("Tasks Supporting the Path to Net Zero")
    st.dataframe(tasks)

    st.header("Net Zero Path Timeline")
    scatter_chart = px.scatter(
        tasks,
        x="Deadline",
        y="Task",
        size="Completion (%)",
        color="Owner",
        title="Net Zero Path Timeline",
        labels={"Deadline": "Timeline", "Task": "Tasks", "Completion (%)": "Completion (%)"},
        height=600
    )
    scatter_chart.update_traces(marker=dict(symbol="circle", opacity=0.8))
    scatter_chart.update_layout(xaxis_title="Timeline", yaxis_title="Tasks", showlegend=True)
    st.plotly_chart(scatter_chart, use_container_width=True)

    # 2.4 Dynamic Decision-Making Tool (Slider for Reductions)
    st.subheader("Adjust Task Priorities or Deadlines")
    selected_task = st.selectbox("Select a Task to Analyze:", tasks["Task"].unique())
    selected_task_details = tasks[tasks["Task"] == selected_task]

    st.write("**Selected Task Details:**")
    st.write(selected_task_details)

    adjusted_deadline = st.date_input(
        f"Adjust Deadline for {selected_task}:",
        pd.to_datetime(selected_task_details["Deadline"].values[0])
    )
    adjusted_priority = st.slider(
        f"Set Priority for {selected_task}:",
        min_value=1, max_value=5, value=3
    )

    st.write(f"Adjusted Deadline: {adjusted_deadline}")
    st.write(f"Adjusted Priority: {adjusted_priority}")

    # 2.5 Overall Compliance Progress
    st.header("Overall Compliance Progress")
    compliance_summary = pd.DataFrame({
        "Track": ["Regulatory Compliance", "Beyond Compliance Initiatives"],
        "Total Tasks": [len(compliance_data), len(beyond_compliance_data)],
        "Completed": [
            compliance_data["Status"].value_counts().get("Completed", 0),
            beyond_compliance_data["Completion (%)"].apply(lambda x: 100 if x == 100 else 0).sum()
        ],
        "In Progress": [
            compliance_data["Status"].value_counts().get("In Progress", 0),
            beyond_compliance_data["Completion (%)"].apply(lambda x: 1 if 0 < x < 100 else 0).sum()
        ],
        "Not Started": [
            compliance_data["Status"].value_counts().get("Not Started", 0),
            beyond_compliance_data["Completion (%)"].apply(lambda x: 1 if x == 0 else 0).sum()
        ]
    })
    st.dataframe(compliance_summary)

    display_footer()

# ====================== 3) COMPLIANCE & REGULATORY =================
elif page == "Compliance & Regulatory":
    display_logos()

    st.title("Compliance & Regulatory")
    st.write("Track regulatory compliance, climate risk, and strategic ESG initiatives under global frameworks.")

    # --- 3.1 Regulatory Compliance Overview ---
    st.header("Regulatory Compliance")
    compliance_data = pd.DataFrame({
        "Regulation": [
            "Proper Conduct of Banking Business Directive 345",
            "Net Zero 2050 (NGFS Scenarios)",
            "EU Green Taxonomy",
            "Corporate Sustainability Reporting Directive (CSRD)",
            "Task Force on Climate-related Financial Disclosures (TCFD)",
            "Israeli Securities Authority ESG Reporting"
        ],
        "Requirement": [
            "Climate risk disclosures and portfolio analysis",
            "Alignment with international climate targets",
            "Classification of green finance activities",
            "Mandatory sustainability reporting",
            "Risk assessment for climate change impacts",
            "Disclosure of ESG-related activities and goals"
        ],
        "Status": ["In Progress", "Completed", "In Progress", "Not Started", "Completed", "In Progress"],
        "Deadline": ["2025-12-31", "2023-12-31", "2024-06-30", "2025-12-31", "2023-12-31", "2024-12-31"],
        "Owner": ["Risk Management", "Sustainability Team", "Finance", "Legal", "Sustainability Team", "Legal"]
    })
    st.dataframe(compliance_data)

    # --- 3.2 Beyond Compliance Initiatives ---
    st.header("Beyond Compliance Initiatives")
    beyond_compliance_data = pd.DataFrame({
        "Initiative": [
            "Allocate NIS 35 billion to green financing by 2030",
            "Reduce operational emissions by 20% by 2030",
            "Achieve 100% digital communication by 2024",
            "Transition all data centers to renewable energy by 2035",
            "Retrofit office buildings for energy efficiency by 2028",
            "Offset 100% of unavoidable emissions by 2040",
            "Sustainability-linked loans totaling NIS 1.48 billion",
            "Facilitate ESG-focused investment products"
        ],
        "Target Year": [2030, 2030, 2024, 2035, 2028, 2040, 2023, 2023],
        "Completion (%)": [45, 20, 80, 15, 25, 5, 100, 100],
        "Owner": [
            "Finance", "Sustainability Team", "IT Department", "IT Department",
            "Operations", "Legal", "Finance", "Finance"
        ]
    })
    st.dataframe(beyond_compliance_data)

    # --- 3.3 Radar/Pentagon Chart: Bank vs International Regulation ---
    st.header("Bank vs. International Regulatory Alignment (Radar Chart)")
    st.write("Visualize Bank Leumi’s alignment scores across multiple regulations/frameworks in a pentagon-style chart.")

    radar_df = pd.DataFrame({
        "Guideline": [
            "TCFD", 
            "EU Green Taxonomy", 
            "CSRD", 
            "IFRS S2", 
            "Net Zero 2050"
        ],
        "Bank Leumi (%)": [85, 70, 65, 75, 80],
        "International Best Practice (%)": [90, 85, 80, 85, 90],
    })
    # Melt the data for Plotly
    radar_melted = radar_df.melt(
        id_vars=["Guideline"], 
        var_name="Entity", 
        value_name="Score"
    )

    radar_chart = px.line_polar(
        radar_melted,
        r="Score",
        theta="Guideline",
        color="Entity",
        line_close=True,
        title="Radar Chart: Bank Leumi vs International Best Practices",
        range_r=[0, 100],  # ensures 0-100 scale
        height=600
    )
    st.plotly_chart(radar_chart, use_container_width=True)

    # --- 3.4 Climate Risk Overview ---
    st.header("Climate Risk Overview and Comparison")
    risks_comparison_data = pd.DataFrame({
        "Risk Type": ["Physical", "Transition", "Liability"],
        "Bank Leumi Score": [75, 65, 50],
        "EU Benchmark": [80, 70, 60],
        "ECB Compliance (%)": [85, 75, 65],
        "Alignment with TCFD (%)": [90, 80, 70]
    })
    st.write("Comparison of Bank Leumi’s climate risk scores to international benchmarks:")
    st.dataframe(risks_comparison_data, use_container_width=True)

    st.subheader("Risk Scores vs International Benchmarks")
    comparison_chart = px.bar(
        risks_comparison_data.melt(id_vars=["Risk Type"], var_name="Metric", value_name="Score"),
        x="Risk Type",
        y="Score",
        color="Metric",
        barmode="group",
        title="Comparison of Bank Leumi’s Climate Risk Scores to EU Benchmarks",
        height=600
    )
    st.plotly_chart(comparison_chart, use_container_width=True)

    # --- Define task_tracker before using it ---
    task_tracker = pd.DataFrame({
        "Task": [
            "Conduct climate scenario analysis for credit portfolio",
            "Implement flood and heat risk assessments for real estate collateral",
            "Develop ESG-focused investment products",
            "Expand sustainability-linked loans by 10% annually",
            "Increase procurement of renewable energy for operations",
            "Complete office energy retrofitting by 2028",
            "Enhance ESG reporting transparency by 2024",
            "Introduce climate risk mitigation training for staff"
        ],
        "Deadline": [
            "2024-06-30", "2025-12-31", "2023-12-31", "2024-12-31",
            "2025-12-31", "2028-12-31", "2024-12-31", "2023-12-31"
        ],
        "Status": [
            "In Progress", "Not Started", "Completed", "In Progress",
            "In Progress", "Not Started", "In Progress", "Completed"
        ],
        "Owner": [
            "Risk Management", "Risk Management", "Finance", "Finance",
            "Operations", "Operations", "Sustainability Team", "HR"
        ]
    })

    # Gantt Chart for tasks
    gantt_chart = px.scatter(
        task_tracker,
        x="Deadline",
        y="Task",
        color="Status",
        title="Task Timeline for Compliance & Regulatory",
        labels={"Deadline": "Timeline", "Task": "Tasks"},
        height=600
    )
    st.plotly_chart(gantt_chart, use_container_width=True)

    # Dynamic Decision-Making Tool
    st.subheader("Adjust Task Priorities or Deadlines")
    selected_task = st.selectbox("Select a Task to Analyze:", task_tracker["Task"].unique())
    selected_task_details = task_tracker[task_tracker["Task"] == selected_task]

    st.write("**Selected Task Details:**")
    st.write(selected_task_details)

    adjusted_deadline = st.date_input(
        f"Adjust Deadline for {selected_task}:",
        pd.to_datetime(selected_task_details["Deadline"].values[0])
    )
    adjusted_priority = st.slider(
        f"Set Priority for {selected_task}:",
        min_value=1, max_value=5, value=3
    )

    st.write(f"Adjusted Deadline: {adjusted_deadline}")
    st.write(f"Adjusted Priority: {adjusted_priority}")

    # 3.5 Overall Compliance Progress
    st.header("Overall Compliance Progress")
    compliance_summary = pd.DataFrame({
        "Track": ["Regulatory Compliance", "Beyond Compliance Initiatives"],
        "Total Tasks": [len(compliance_data), len(beyond_compliance_data)],
        "Completed": [
            compliance_data["Status"].value_counts().get("Completed", 0),
            beyond_compliance_data["Completion (%)"].apply(lambda x: 100 if x == 100 else 0).sum()
        ],
        "In Progress": [
            compliance_data["Status"].value_counts().get("In Progress", 0),
            beyond_compliance_data["Completion (%)"].apply(lambda x: 1 if 0 < x < 100 else 0).sum()
        ],
        "Not Started": [
            compliance_data["Status"].value_counts().get("Not Started", 0),
            beyond_compliance_data["Completion (%)"].apply(lambda x: 1 if x == 0 else 0).sum()
        ]
    })
    st.dataframe(compliance_summary)

    display_footer()

# ====================== 4) FINANCIAL ANALYSIS ======================
elif page == "Financial Analysis":
    display_logos()

    st.title("Financial Analysis")
    st.write(
        "Explore carbon pricing scenarios, operating/capital expenditures for ESG projects, "
        "and the potential financial impact of climate risks."
    )

    # 4.1 Carbon Pricing Scenarios
    st.header("Carbon Pricing & Tax Scenarios")
    st.write("Analyze the potential cost impact of various carbon tax rates on Bank Leumi’s emissions.")

    # Example simple slider for carbon tax
    carbon_tax_rate = st.slider("Select Carbon Tax Rate (USD/ton CO₂)", 0, 200, 50)
    # Example total bank emissions (Scope 1 + 2) just as a placeholder
    total_scope_1_2_emissions = 30000  # adjust as needed (in tons CO₂)

    estimated_cost = total_scope_1_2_emissions * carbon_tax_rate
    st.write(f"**Estimated Annual Carbon Tax**: ${estimated_cost:,.0f} at {carbon_tax_rate} USD/ton")

    # 4.2 CAPEX vs. OPEX for Key ESG Projects
    st.header("Capital & Operating Expenditure (CAPEX/OPEX) for ESG Projects")
    projects_data = pd.DataFrame({
        "Project": ["Office Retrofit", "EV Fleet Transition", "Renewable Data Centers"],
        "CAPEX (NIS millions)": [35, 50, 75],
        "Annual OPEX Savings (NIS millions)": [5, 8, 15],
        "Payback (Years)": [7, 6, 5]
    })
    st.dataframe(projects_data)

    # Simple bar chart to visualize CAPEX
    capex_chart = px.bar(
        projects_data,
        x="Project",
        y="CAPEX (NIS millions)",
        title="CAPEX for Major ESG Projects",
        height=400
    )
    st.plotly_chart(capex_chart, use_container_width=True)

    # 4.3 ROI/NPV Calculations (Illustrative)
    st.header("Estimated ROI/NPV (Illustrative)")
    st.write(
        "Below is a hypothetical ROI calculation for each project, assuming a discount rate of 5%. "
        "Adapt this to real data for precise analysis."
    )
    # We'll just show them as made-up values
    roi_data = pd.DataFrame({
        "Project": ["Office Retrofit", "EV Fleet Transition", "Renewable Data Centers"],
        "ROI (%)": [12, 15, 20],
        "NPV (NIS millions)": [10, 15, 30]
    })
    st.table(roi_data)

    display_footer()

# ====================== 5) DECISION SUPPORT TOOLS ======================
elif page == "Decision Support Tools":
    display_logos()

    st.title("Decision Support Tools")
    st.write(
        """
        This section brings together key ESG metrics, scenario modeling, and guidance 
        from international frameworks. It aims to help Bank Leumi make evidence-based 
        strategic decisions to reach its sustainability targets.
        """
    )

    # 5.1 Key Performance Indicators (KPIs)
    st.header("Key Performance Indicators (KPIs)")
    st.write(
        "Below is a snapshot of crucial ESG metrics aligned with Bank Leumi’s strategy "
        "and global benchmarks (TCFD, SASB, IFRS S2)."
    )
    kpi_data = pd.DataFrame({
        "KPI": [
            "Carbon Intensity (kg CO₂e / million NIS assets)", 
            "Green Financing Volume (NIS billions)",
            "Renewable Energy in Operations (%)",
            "Female Representation in Management (%)",
            "Supplier ESG Compliance Rate (%)"
        ],
        "Current Value": [320, 18, 25, 40, 60],
        "2025 Target": [250, 25, 40, 45, 75],
        "2030 Target": [150, 40, 80, 50, 90]
    })
    st.table(kpi_data)
    
    # 5.2 Scenario Modeling Example
    st.header("Scenario Modeling")
    st.write(
        "Use the sliders below to explore different scenarios for carbon reduction and "
        "green financing expansion. This helps decision-makers understand potential tradeoffs."
    )
    
    # Carbon Reduction Slider
    carbon_reduction = st.slider("Carbon Reduction by 2030 (%)", 0, 100, 30)
    green_financing = st.slider("Green Financing Growth (NIS billions by 2030)", 0, 50, 20)
    
    base_carbon_intensity = 320  # from KPI table
    new_carbon_intensity = base_carbon_intensity * (1 - carbon_reduction / 100)
    base_green_finance = 18
    new_green_finance = base_green_finance + green_financing
    
    st.write(f"**Projected Carbon Intensity**: {new_carbon_intensity:.2f} kg CO₂e / million NIS")
    st.write(f"**Projected Green Financing Volume**: {new_green_finance:.2f} NIS billions")
    
    # 5.3 Stakeholder Engagement & Collaboration
    st.header("Stakeholder Engagement & Collaboration")
    st.write(
        """
        Effective ESG implementation requires cross-department collaboration and external engagement 
        with regulators, investors, and civil society organizations. The table below highlights 
        recommended stakeholders and potential roles.
        """
    )
    stakeholders = pd.DataFrame({
        "Stakeholder": [
            "Risk Management", "Finance", "HR", "IT Department", 
            "Operations", "Regulators", "NGOs/Civil Society"
        ],
        "Role": [
            "Evaluate and integrate climate risks into credit decisions",
            "Structure green financing instruments, measure ROI of ESG",
            "Oversee employee engagement/training on ESG topics",
            "Implement technology solutions for ESG data and monitoring",
            "Optimize resource use (energy, water, waste) in daily operations",
            "Provide regulatory guidelines and oversight on ESG disclosures",
            "Offer independent insights on community/environmental needs"
        ]
    })
    st.table(stakeholders)
    
    # 5.4 Recommended Actions (Best Practices from Global Banks)
    st.header("Recommended Actions for Bank Leumi")
    st.write(
        """
        These recommendations draw on best practices from leading global banks 
        (e.g., Barclays, HSBC, RBC) and align with international guidelines 
        (NGFS scenarios, TCFD).
        """
    )
    recommendations = [
        "Establish Science-Based Targets for GHG emissions reductions (aligned with SBTi).",
        "Expand green bond issuance and sustainability-linked loans to enhance market positioning.",
        "Fully integrate climate risk in loan origination systems and credit risk models.",
        "Adopt IFRS S2 (Sustainability Disclosure) once finalized for standardized reporting.",
        "Implement a holistic employee training program on ESG, ensuring cross-functional literacy.",
        "Introduce annual reporting on progress towards Net Zero, referencing TCFD recommendations."
    ]
    for idx, rec in enumerate(recommendations, start=1):
        st.markdown(f"{idx}. {rec}")

    # 5.5 Reference to Bank Leumi ESG Report
    st.header("Alignment with Bank Leumi ESG Report")
    st.write(
        """
        Bank Leumi's ESG report emphasizes climate risk management, community investment, 
        and responsible finance. This Decision Support Tool helps track progress on those 
        commitments, bridging the gap between high-level targets and day-to-day actions.
        """
    )
    
    st.write(
        "By integrating data from Bank Leumi's existing sustainability disclosures and the frameworks "
        "mentioned, this tool can evolve into a real-time ESG performance cockpit."
    )

    display_footer()

# ====================== 6) KPI METRICS OVERVIEW ======================
elif page == "KPI Metrics Overview":
    display_logos()

    st.title("KPI Metrics Overview")
    st.write("Track and analyze key performance indicators (KPIs) to measure Bank Leumi's ESG performance.")

    # --- 1. KPI Data ---
    st.header("Key Performance Indicators (KPIs)")
    kpi_data_path = os.path.join(os.path.dirname(__file__), "data", "kpi_data.csv")
    if os.path.exists(kpi_data_path):
        kpi_data = pd.read_csv(kpi_data_path)
        st.table(kpi_data)
    else:
        st.warning("KPI data file not found in the data folder.")

    # --- 2. KPI Progress Visualization ---
    st.header("KPI Progress Towards Targets")
    # Melt the data for plotting
    kpi_melted = kpi_data.melt(
        id_vars=["KPI"], 
        var_name="Year", 
        value_name="Value"
    )

    kpi_chart = px.bar(
        kpi_melted,
        x="KPI",
        y="Value",
        color="Year",
        barmode="group",
        title="KPI Progress Towards Targets",
        labels={"Value": "Value", "KPI": "Key Performance Indicator"},
        height=600
    )
    st.plotly_chart(kpi_chart, use_container_width=True)

    # --- 3. KPI Trend Over Time ---
    st.header("KPI Trend Over Time")
    # Example trend data (for illustrative purposes)
    trend_data = pd.DataFrame({
        "Year": [2020, 2021, 2022, 2023, 2024, 2025, 2030],
        "Carbon Intensity (kg CO₂e / million NIS assets)": [400, 350, 330, 320, 300, 250, 150],
        "Green Financing Volume (NIS billions)": [10, 12, 15, 16, 18, 25, 40],
        "Renewable Energy in Operations (%)": [10, 15, 18, 20, 25, 40, 80],
        "Female Representation in Management (%)": [30, 35, 38, 40, 42, 45, 50],
        "Supplier ESG Compliance Rate (%)": [50, 55, 58, 60, 65, 75, 90]
    })
    
    # Plotly Line Chart
    trend_chart = px.line(
        trend_data,
        x="Year",
        y=[
            "Carbon Intensity (kg CO₂e / million NIS assets)", 
            "Green Financing Volume (NIS billions)",
            "Renewable Energy in Operations (%)",
            "Female Representation in Management (%)",
            "Supplier ESG Compliance Rate (%)"
        ],
        title="KPI Trend Over Time",
        labels={"Value": "Value", "Year": "Year"},
        height=600
    )
    st.plotly_chart(trend_chart, use_container_width=True)

    # --- 4. KPI Comparison to Industry Benchmarks ---
    st.header("KPI Comparison to Industry Benchmarks")
    # Example benchmark data
    benchmark_data = pd.DataFrame({
        "KPI": [
            "Carbon Intensity (kg CO₂e / million NIS assets)", 
            "Green Financing Volume (NIS billions)",
            "Renewable Energy in Operations (%)",
            "Female Representation in Management (%)",
            "Supplier ESG Compliance Rate (%)"
        ],
        "Bank Leumi": [250, 25, 40, 45, 75],
        "Industry Average": [300, 20, 35, 40, 70],
        "Best in Class": [150, 40, 80, 50, 90]
    })
    st.table(benchmark_data)

    # Plotly Grouped Bar Chart
    benchmark_melted = benchmark_data.melt(
        id_vars=["KPI"], 
        var_name="Entity", 
        value_name="Value"
    )
    
    benchmark_chart = px.bar(
        benchmark_melted,
        x="KPI",
        y="Value",
        color="Entity",
        barmode="group",
        title="KPI Comparison to Industry Benchmarks",
        labels={"Value": "Value", "KPI": "Key Performance Indicator"},
        height=600
    )
    st.plotly_chart(benchmark_chart, use_container_width=True)

    # --- 5. Summary of KPI Achievements ---
    st.header("Summary of KPI Achievements")
    summary_data = pd.DataFrame({
        "KPI": [
            "Carbon Intensity Reduction",
            "Increase in Green Financing",
            "Expansion of Renewable Energy Use",
            "Growth in Female Management",
            "Enhancement of Supplier ESG Compliance"
        ],
        "Status": [
            "On Track", "Achieved 2025 Target", "Behind Schedule", "On Track", "Achieved 2025 Target"
        ]
    })
    st.table(summary_data)

    display_footer()

# ====================== 7) OTHER PAGES ======================
# (Include your existing Portfolio Carbon Analysis, Compliance & Regulatory, Financial Analysis, Decision Support Tools pages here)

# ====================== End of Script ======================