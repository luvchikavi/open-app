

from pyvis.network import Network
import math
import subprocess
import os

# Initialize the network with a modern look
net = Network(height="800px", width="100%", bgcolor="#ffffff", font_color="black", notebook=False)

# Define central data (Heart)
central_node = {
    'label': "🏦 Live Data\nScope 1: 1500\nScope 2: 3000\nScope 3: 4500",
    'shape': 'circle',
    'color': {
        'background': '#17becf',
        'border': '#000000'
    },
    'font': {'size': 16, 'face': 'Arial', 'bold': True},
    'size': 60,
    'title': "Central Emissions Data:\nScope 1: 1500 tons CO₂e\nScope 2: 3000 tons CO₂e\nScope 3: 4500 tons CO₂e"
}

# Add central node with 'central' as the node ID
net.add_node('central', label=central_node['label'], shape=central_node['shape'],
             color=central_node['color'], font=central_node['font'],
             size=central_node['size'], title=central_node['title'])

# Define modules (Spokes/Petals)
modules = [
    {'id': 'compliance', 'label': "⚖️ Compliance & Regulations", 'color': '#1f77b4'},
    {'id': 'finance', 'label': "💰 Finance & Costs", 'color': '#ff7f0e'},
    {'id': 'operations', 'label': "🏭 Operations & Supply Chain", 'color': '#2ca02c'},
    {'id': 'benchmarking', 'label': "📊 Benchmarking & Market Data", 'color': '#d62728'},
    {'id': 'tasks', 'label': "📋 Task & Goal Tracking", 'color': '#9467bd'},
    {'id': 'waste', 'label': "♻️ Waste Management", 'color': '#8c564b'}
]

# Calculate angles for modules to position them evenly around the central node
num_modules = len(modules)
angle_gap = 360 / num_modules

for i, module in enumerate(modules):
    angle_deg = angle_gap * i
    angle_rad = math.radians(angle_deg)
    x = 8 * math.cos(angle_rad)
    y = 8 * math.sin(angle_rad)
    
    module_node = {
        'label': module['label'],
        'shape': 'circle',
        'color': {
            'background': module['color'],
            'border': '#000000'
        },
        'font': {'size': 14, 'face': 'Arial', 'bold': False},
        'size': 40,
        'title': f"{module['label']} Module"
    }
    
    # Add module node with its own ID
    net.add_node(module['id'], label=module_node['label'], shape=module_node['shape'],
                color=module_node['color'], font=module_node['font'],
                size=module_node['size'], title=module_node['title'])
    
    # Add edge from central to module
    net.add_edge('central', module['id'], color='#cccccc', width=2)

# Customize the physics for a better layout
net.force_atlas_2based(gravity=-200, central_gravity=0.3, spring_length=200, spring_strength=0.1, damping=0.4)

# Enhance network appearance with rounded edges and modern aesthetics
net.set_options("""
var options = {
  "nodes": {
    "font": {
      "face": "Arial",
      "size": 14,
      "color": "#000000"
    },
    "borderWidth": 2,
    "shadow": {
      "enabled": true,
      "color": "#000000",
      "size": 10,
      "x": 5,
      "y": 5
    }
  },
  "edges": {
    "color": {
      "inherit": false,
      "color": "#cccccc"
    },
    "smooth": false
  },
  "physics": {
    "forceAtlas2Based": {
      "gravitationalConstant": -200,
      "centralGravity": 0.3,
      "springLength": 200,
      "springStrength": 0.1,
      "damping": 0.4
    },
    "maxVelocity": 50,
    "solver": "forceAtlas2Based"
  }
}
"""
)

# Save the network to an HTML file
net.show("decision_tool_architecture_pyvis.html")

# Define LaTeX document path
latex_path = "technical_notebook.tex"
pdf_output_path = "technical_notebook.pdf"

# Compile LaTeX to PDF
if os.path.exists(latex_path):
    try:
        subprocess.run(['pdflatex', latex_path], check=True)
        print(f"Successfully generated PDF: {pdf_output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during LaTeX compilation: {e}")
else:
    print(f"LaTeX file not found at path: {latex_path}")