import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Graph:

    def __init__(self, df, value_m, pair_name):
        self.df = df
        self.value_m = value_m
        self.pair_name = pair_name

    def graphic(self):
        try:
            specs = [[{"secondary_y": True}], [{"secondary_y": False}], [{"secondary_y": True}]]

            if len(self.value_m) == 0:
                fig = make_subplots(rows=3, cols=1,
                                    shared_xaxes=True,
                                    specs=specs,
                                    subplot_titles=("<b>" + self.pair_name + " Graph<b>", "<b>Stochastic oscilator<b>", ""))
            else:
                fig = make_subplots(rows=3, cols=1,
                                    shared_xaxes=True,
                                    specs=specs,
                                    subplot_titles=("<b>" + self.pair_name + " Graph<b>", "<b>Stochastic oscilator<b>", "<b>Moving Average<b>"))

            fig.add_trace(go.Candlestick(x=self.df.index,
                                         open=self.df['open'],
                                         close=self.df['close'],
                                         low=self.df['low'],
                                         high=self.df['high']),
                          secondary_y=False,
                          row=1, col=1)

            for m in self.value_m:
                fig.add_trace(go.Scatter(x=self.df.index, y=self.df['moving_average_' + str(m)]), secondary_y=True,
                              row=1, col=1)
                fig.add_trace(go.Scatter(x=self.df.index, y=self.df['moving_average_' + str(m)]), secondary_y=False,
                              row=3, col=1)

            fig.add_trace(go.Scatter(x=self.df.index, y=self.df.stochastic_osc, line=dict(color="black")), secondary_y=False,
                          row=2, col=1)
            fig.update_xaxes(row=1, col=1, rangeslider_thickness=0.05)
            fig.update_layout(width=1000, height=900)
            fig.update_layout(xaxis_showticklabels=True, xaxis2_showticklabels=True)
            return fig

        except Exception as e:
            print(str(e) + 'has occurred')
            return