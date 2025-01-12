# decision_tool_architecture_pyvis.py

from pyvis.network import Network
import math

# Initialize the network
net = Network(height="800px", width="100%", bgcolor="#ffffff", font_color="black")

# Define central data (Heart)
central_node = {
    'id': 'central',
    'label': "🏦 Live Data\nScope 1: 1500\nScope 2: 3000\nScope 3: 4500",
    'shape': 'circle',
    'color': {
        'background': '#17becf',
        'border': 'black'
    },
    'font': {'size': 16, 'face': 'Arial', 'bold': True},
    'size': 50
}

net.add_node(**central_node)

# Define modules (Spokes/Petals)
modules = [
    {'id': 'compliance', 'label': "⚖️ Compliance & Regulations", 'color': '#1f77b4'},
    {'id': 'finance', 'label': "💰 Finance & Costs", 'color': '#ff7f0e'},
    {'id': 'operations', 'label': "🏭 Operations & Supply Chain", 'color': '#2ca02c'},
    {'id': 'benchmarking', 'label': "📊 Benchmarking & Market Data", 'color': '#d62728'},
    {'id': 'tasks', 'label': "📋 Task & Goal Tracking", 'color': '#9467bd'},
    {'id': 'waste', 'label': "♻️ Waste Management", 'color': '#8c564b'}
]

# Calculate positions for modules around the central node
num_modules = len(modules)
angle_gap = 360 / num_modules

for i, module in enumerate(modules):
    angle_deg = angle_gap * i
    angle_rad = math.radians(angle_deg)
    x = math.cos(angle_rad)
    y = math.sin(angle_rad)
    
    module_node = {
        'id': module['id'],
        'label': module['label'],
        'shape': 'circle',
        'color': {
            'background': module['color'],
            'border': 'black'
        },
        'font': {'size': 14, 'face': 'Arial', 'bold': False},
        'size': 30
    }
    
    net.add_node(**module_node)
    net.add_edge('central', module['id'], color='#cccccc', width=2)

# Customize the physics for a better layout
net.force_atlas_2based(gravity=-50, central_gravity=0.01, spring_length=200, spring_strength=0.08, damping=0.4)

# Enable physics for dynamic layout
net.show_buttons(filter_=['physics'])

# Save the network to an HTML file
net.show("decision_tool_architecture_pyvis.html")