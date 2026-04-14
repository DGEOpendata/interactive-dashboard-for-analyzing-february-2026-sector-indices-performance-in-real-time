python
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Load dataset
data = pd.read_excel('Indices_Summary_FEB_0.xlsx')
data['Date'] = pd.to_datetime(data['Date'])

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1('February 2026 Sector Indices Performance Dashboard'),
    dcc.Dropdown(
        id='index-dropdown',
        options=[
            {'label': 'FADGI', 'value': 'FADGI'},
            {'label': 'FADX15', 'value': 'FADX15'},
            {'label': 'FADSI', 'value': 'FADSI'},
            {'label': 'FADXI15', 'value': 'FADXI15'},
            {'label': 'FADXSI', 'value': 'FADXSI'}
        ],
        value='FADX15',
        multi=False,
        placeholder='Select an index'
    ),
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=data['Date'].min(),
        end_date=data['Date'].max(),
        display_format='YYYY-MM-DD'
    ),
    dcc.Graph(id='performance-graph'),
    dcc.Graph(id='daily-change-graph')
])

# Callbacks
@app.callback(
    [
        Output('performance-graph', 'figure'),
        Output('daily-change-graph', 'figure')
    ],
    [
        Input('index-dropdown', 'value'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date')
    ]
)
def update_graphs(selected_index, start_date, end_date):
    filtered_data = data[(data['Index'] == selected_index) & 
                        (data['Date'] >= pd.to_datetime(start_date)) & 
                        (data['Date'] <= pd.to_datetime(end_date))]

    # Performance Graph
    perf_fig = go.Figure()
    perf_fig.add_trace(go.Scatter(
        x=filtered_data['Date'],
        y=filtered_data['Closing Value'],
        mode='lines+markers',
        name='Closing Value'
    ))

    perf_fig.update_layout(
        title=f'{selected_index} Performance Over Time',
        xaxis_title='Date',
        yaxis_title='Closing Value'
    )

    # Daily Change Graph
    daily_change_fig = go.Figure()
    daily_change_fig.add_trace(go.Bar(
        x=filtered_data['Date'],
        y=filtered_data['Daily % Change'],
        name='Daily % Change'
    ))

    daily_change_fig.update_layout(
        title=f'{selected_index} Daily Percentage Change',
        xaxis_title='Date',
        yaxis_title='Percentage Change (%)'
    )

    return perf_fig, daily_change_fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
