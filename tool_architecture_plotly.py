# tool_architecture_plotly.py

import plotly.graph_objects as go
import math
import os

# Define central data (Heart)
central_metrics = {
    'Scope 1': 1500,  # Example values in tons CO2e
    'Scope 2': 3000,
    'Scope 3': 4500
}

# Define modules (Spokes/Petals)
modules = [
    {'name': 'Compliance & Regulations', 'icon': '⚖️', 'color': '#1f77b4'},
    {'name': 'Finance & Costs', 'icon': '💰', 'color': '#ff7f0e'},
    {'name': 'Operations & Supply Chain', 'icon': '🏭', 'color': '#2ca02c'},
    {'name': 'Benchmarking & Market Data', 'icon': '📊', 'color': '#d62728'},
    {'name': 'Task & Goal Tracking', 'icon': '📋', 'color': '#9467bd'},
    {'name': 'Waste Management', 'icon': '♻️', 'color': '#8c564b'}
]

# Calculate angles for modules to position them evenly around the central node
num_modules = len(modules)
angle_gap = 360 / num_modules

# Initialize Plotly figure
fig = go.Figure()

# Add central node
central_label = f"🏦 Live Data<br>Scope 1: {central_metrics['Scope 1']}<br>Scope 2: {central_metrics['Scope 2']}<br>Scope 3: {central_metrics['Scope 3']}"
fig.add_trace(go.Scatter(
    x=[0],
    y=[0],
    mode='markers+text',
    marker=dict(
        size=60,
        color='#17becf',
        line=dict(width=2, color='DarkSlateGrey')
    ),
    text=[central_label],
    textposition='middle center',
    hoverinfo='text'
))

# Add module nodes and edges
for i, module in enumerate(modules):
    angle_deg = angle_gap * i
    angle_rad = math.radians(angle_deg)
    x = 8 * math.cos(angle_rad)
    y = 8 * math.sin(angle_rad)
    
    # Add edge
    fig.add_trace(go.Scatter(
        x=[0, x],
        y=[0, y],
        mode='lines',
        line=dict(color='#cccccc', width=2),
        hoverinfo='none'
    ))
    
    # Add module node
    module_label = f"{module['icon']}<br>{module['name']}"
    fig.add_trace(go.Scatter(
        x=[x],
        y=[y],
        mode='markers+text',
        marker=dict(
            size=40,
            color=module['color'],
            line=dict(width=2, color='DarkSlateGrey')
        ),
        text=[module_label],
        textposition='middle center',
        hoverinfo='text'
    ))

# Update layout for modern aesthetics
fig.update_layout(
    title={
        'text': "Bank Leumi Environmental Compliance and Management Tool Architecture",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    showlegend=False,
    hovermode='closest',
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-10, 10]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-10, 10]),
    plot_bgcolor='white',
    margin=dict(l=0, r=0, t=100, b=0)
)

# Customize hover information
for trace in fig.data:
    if trace.mode == 'markers+text':
        trace.hoverinfo = 'text'

# Save the network to an HTML file
output_html = "decision_tool_architecture_plotly.html"
fig.write_html(output_html)
print(f"Visualization saved to {output_html}")

# Optionally, open the HTML file automatically (uncomment if desired)
# import webbrowser
# webbrowser.open('file://' + os.path.realpath(output_html))