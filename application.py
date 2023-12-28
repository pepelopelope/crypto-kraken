# Importar las bibliotecas necesarias
import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
# Importar módulos personalizados
from kraken_data import krakenex_data_import, get_ohlc_data
from technical_indicators import Moving_Average, StochasticOscillator
from graphing import Graph

try:
    # Importar datos desde Kraken y asignar valores a 'k' y 'pairs'
    k, pairs = krakenex_data_import()

    # Crear una aplicación Dash y definir hojas de estilo externas
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

    # Definir el diseño de la aplicación usando HTML y componentes Dash
    app.layout = html.Div([
        # Contenedor para la selección de la media móvil
        html.Div(children=[
            html.Label('Select the average moving'),
            dcc.Dropdown(options=[{'label': slot, 'value': slot} for slot in [10, 20, 30, 40, 50, 60]],
                         multi=True, id='average-dropdown'),
        ], style={'padding': 10, 'flex': 1, 'justifyContent': 'left'}),

        # Contenedor para la selección de activos
        html.Div(children=[
            html.Label('Select an asset'),
            dcc.Dropdown(options=[{'label': pair, 'value': pair} for pair in pairs], id='demo-dropdown',
                         style={'width': '1000px'}),
            html.Div(id='dd-output-container')
        ], style={'padding': 10, 'flex': 1}),

        # Contenedor para la selección del intervalo del par
        html.Div(children=[
            html.Label('Select the pair interval'),
            dcc.Dropdown(options=[{'label': interval, 'value': interval} for interval in
                                 [1, 5, 15, 30, 60, 240, 1440, 10080, 21600]], value=10080,
                         multi=False, id='interval-dropdown'),
        ], style={'padding': 10, 'flex': 1, 'justifyContent': 'right'})
    ], style={'display': 'flex'})

    # Definir una callback para actualizar la figura basada en las entradas del usuario
    @app.callback(
        Output('dd-output-container', 'children'),
        [Input('demo-dropdown', 'value'),
         Input('average-dropdown', 'value'),
         Input('interval-dropdown', 'value')]
    )
    def update_figure(value, value_m, value_i):
        try:
            # Si no se selecciona un valor, no hacer nada
            if value is None:
                return ""
            else:
                # Obtener los datos OHLC del par seleccionado
                df, last = get_ohlc_data(k, value, interval=value_i)

                # Calcular la media móvil si se seleccionaron valores
                if (value_m is None) == False:
                    for m in value_m:
                        df = Moving_Average(m, df).calculate()
                else:
                    value_m = []

                # Calcular el oscilador estocástico
                df = StochasticOscillator(df).calculate()

                # Devolver un gráfico con los datos calculados
                return html.Div([
                    dcc.Graph(
                        id='example-graph',
                        figure=Graph(df, value_m, value).graphic())
                ])
        except Exception as e:
            print('This problem has occurred in the figure update: ' + str(e))

    # Ejecutar la aplicación si este script es el principal
    if __name__ == '__main__':
        app.run_server(debug=True, use_reloader=False)

except Exception as e:
    print('This problem has occurred: ' + str(e))
