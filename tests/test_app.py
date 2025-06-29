import pytest
from dash import Dash
from app import app  # Replace 'app' if your file is named differently

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")  # Adjust tag if you used h2, etc.
    assert header.text == "Your App Title"  # Replace with actual title

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    chart = dash_duo.find_element("svg")  # Plotly renders in SVG
    assert chart is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.find_element(".dash-radio-items")
    assert radio is not None
  
