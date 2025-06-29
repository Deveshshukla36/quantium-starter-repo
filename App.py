import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px

# Load data
df = pd.read_csv('data/merged_sales_data.csv')  # replace with your actual file

# Ensure date column is datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date and sum sales
sales_by_date = df.groupby('date')['sales'].sum().reset_index()

# Create line chart
fig = px.line(sales_by_date, x='date', y='sales', title='Total Sales Over Time',
              labels={'date': 'Date', 'sales': 'Total Sales ($)'})

# Mark the price change date
fig.add_vline(x='2021-01-15', line_dash="dash", line_color="red", annotation_text="Price Increase", annotation_position="top left")

# Build Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Impact of Pink Morsel Price Increase", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
