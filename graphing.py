# Importar bibliotecas necesarias para crear gráficos interactivos
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Definir una clase llamada 'Graph'
class Graph:

    # Constructor de la clase
    def __init__(self, df, value_m, pair_name):
        # Inicializar las variables de la clase con los datos proporcionados
        self.df = df            # DataFrame con los datos a graficar
        self.value_m = value_m  # Lista de valores para la media móvil
        self.pair_name = pair_name  # Nombre del par de criptomonedas

    # Método para crear gráficos
    def graphic(self):
        try:
            # Definir especificaciones de los subgráficos
            specs = [[{"secondary_y": True}], [{"secondary_y": False}], [{"secondary_y": True}]]

            # Crear figuras con subgráficos dependiendo de si 'value_m' está vacío o no
            if len(self.value_m) == 0:
                fig = make_subplots(rows=3, cols=1, shared_xaxes=True, specs=specs,
                                    subplot_titles=("<b>" + self.pair_name + " Graph<b>", "<b>Stochastic oscilator<b>", ""))
            else:
                fig = make_subplots(rows=3, cols=1, shared_xaxes=True, specs=specs,
                                    subplot_titles=("<b>" + self.pair_name + " Graph<b>", "<b>Stochastic oscilator<b>", "<b>Moving Average<b>"))

            # Añadir el gráfico de velas al primer subgráfico
            fig.add_trace(go.Candlestick(x=self.df.index, open=self.df['open'], close=self.df['close'], low=self.df['low'], high=self.df['high'], name="Graph 1: Candlestick asset chart"),
                          secondary_y=False, row=1, col=1)

            # Añadir medias móviles al gráfico si 'value_m' no está vacío
            for m in self.value_m:
                fig.add_trace(go.Scatter(x=self.df.index, y=self.df['moving_average_' + str(m)], name="Graph 1: moving average" + " " + str(m)), secondary_y=True, row=1, col=1)
                fig.add_trace(go.Scatter(x=self.df.index, y=self.df['moving_average_' + str(m)], name="Graph 3: moving average" + " " + str(m)), secondary_y=False, row=3, col=1)

            # Añadir gráfico del oscilador estocástico
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df.stochastic_osc, line=dict(color="green"), name="Graph 2: Stochastic oscilator K%"), secondary_y=False, row=2, col=1)
            fig.add_trace(go.Scatter(x=self.df.index, y=self.df.stochastic_osc_ma, line=dict(color="red"), name="Graph 2: Stochastic oscilator D%"), secondary_y=False, row=2, col=1)

            # Actualizar configuraciones de los ejes y el tamaño del gráfico
            fig.update_xaxes(row=1, col=1, rangeslider_thickness=0.05)
            fig.update_layout(width=1000, height=900)
            fig.update_layout(xaxis_showticklabels=True, xaxis2_showticklabels=True)

            # Devolver la figura con los gráficos
            return fig

        # Capturar y manejar excepciones
        except Exception as e:
            print(str(e) + 'has occurred')
            return
