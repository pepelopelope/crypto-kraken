import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from kraken_data import krakenex_data_import, get_ohlc_data
from technical_indicators import Moving_Average, StochasticOscillator
from graphing import Graph

try:
    k, pairs = krakenex_data_import()

    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

    app.layout = html.Div([
        html.Div(children=[
            html.Label('Select an asset'),
            dcc.Dropdown(options=[{'label': pair, 'value': pair} for pair in pairs], id='demo-dropdown',
                         style={'width': '1000px'}),

            html.Div(id='dd-output-container')

        ], style={'padding': 10, 'flex': 1}),

        html.Div(children=[

            html.Label('Select the average moving'),
            dcc.Dropdown(options=[{'label': slot, 'value': slot} for slot in [10, 20, 30, 40, 50, 60]],
                         multi=True, id='average-dropdown'),

        ], style={'padding': 10, 'flex': 1}),

        html.Div(children=[

            html.Label('Select the pair interval'),
            dcc.Dropdown(options=[{'label': interval, 'value': interval} for interval in
                                 [1, 5, 15, 30, 60, 240, 1440, 10080, 21600]], value=60,
                         multi=False, id='interval-dropdown'),

        ], style={'padding': 10, 'flex': 1})
    ], style={'display': 'flex', 'justifyContent': 'center'})

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
                df, last = get_ohlc_data(k, value, interval=value_i)

                if (value_m is None) == False:
                    for m in value_m:
                        df = Moving_Average(m, df).calculate()
                else:
                    value_m = []

                df = StochasticOscillator(df).calculate()
                

                return html.Div([
                    dcc.Graph(
                        id='example-graph',
                        figure=Graph(df, value_m, value).graphic())
                ])
        except Exception as e:
            print('This problem has occurred in the figure update: ' + str(e))

    if __name__ == '__main__':
        app.run_server(debug=True, use_reloader=False)

except Exception as e:
    print('This problem has occurred: ' + str(e))
