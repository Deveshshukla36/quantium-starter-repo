import pandas as pd
import dash
from dash import html, dcc, Input, Output
import plotly.express as px

# Load and prepare data
df = pd.read_csv("data/merged_sales_data.csv")
df['date'] = pd.to_datetime(df['date'])

# Setup Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    style={'fontFamily': 'Arial', 'padding': '2rem', 'backgroundColor': '#f9f9f9'},
    children=[
        html.H1("Pink Morsel Sales Trend by Region", style={'textAlign': 'center'}),
        
        html.Div([
            html.Label("Select Region:", style={'fontSize': '18px'}),
            dcc.RadioItems(
                id='region-radio',
                options=[
                    {'label': 'All', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                ],
                value='all',
                labelStyle={'display': 'inline-block', 'marginRight': '15px'}
            ),
        ], style={'textAlign': 'center', 'marginBottom': '20px'}),

        dcc.Graph(id='sales-graph')
    ]
)

# Callback to update chart based on selected region
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    sales_by_date = filtered_df.groupby('date')['sales'].sum().reset_index()

    fig = px.line(
        sales_by_date,
        x='date',
        y='sales',
        title=f"Sales Trend - {selected_region.capitalize()} Region" if selected_region != 'all' else "Sales Trend - All Regions",
        labels={'date': 'Date', 'sales': 'Total Sales ($)'}
    )

    fig.add_vline(
        x='2021-01-15',
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="_
  
