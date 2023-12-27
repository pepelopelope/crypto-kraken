import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from data_import import krakenex_data_import
from indicators import MovingAverageCalculator, RSICalculator

k, pairs = krakenex_data_import()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div([
    html.Div(children=[
        html.Label('Select an asset'),
        dcc.Dropdown(pairs, id='demo-dropdown', style={'width': '1000px'}),
        html.Div(id='dd-output-container')
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Label('Select the average moving'),
        dcc.Dropdown([10, 20, 30, 40, 50, 60], multi=True, id='average-dropdown'),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Label('Select the pair interval'),
        dcc.Dropdown([1, 5, 15, 30, 60, 240, 1440, 10080, 21600], 60, multi=False, id='interval-dropdown'),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flex-direction': 'row'})

@app.callback(
    Output('dd-output-container', 'children'),
    [Input('demo-dropdown', 'value'),
     Input('average-dropdown', 'value'),
     Input('interval-dropdown', 'value')]
)
def update_figure(value, value_m, value_i):
    try:
        if value is None:
            return ""
        else:
            df, last = k.get_ohlc_data(value, interval=value_i)

            if (value_m is None) == False:
                for m in value_m:
                    df = MovingAverageCalculator(df).calculate(m)
            else:
                value_m = []

            df = RSICalculator(df).calculate()

            return html.Div([
                dcc.Graph(
                    id='example-graph',
                    figure=Graph(df, value_m, value).graphic())
            ])
    except Exception as e:
        print('This problem has occurred in the figure update: ' + str(e))

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)