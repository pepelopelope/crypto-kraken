import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
import pandas as pd


class TestKrakenData(unittest.TestCase):

    @patch('kraken_data.krakenex_data_import')
    def test_get_ohlc_data(self, mock_krakenex_data_import):
        # Configurar el comportamiento del objeto mock
        mock_krakenex_data_import.return_value = (MagicMock(), ['BTC/USD', 'ETH/USD'])
        mock_krakenex_data_import.return_value[0].get_ohlc_data.return_value = (pd.DataFrame(), 'last')

        # Importar y ejecutar la función real
        from kraken_data import get_ohlc_data
        df, last = get_ohlc_data(mock_krakenex_data_import.return_value[0], 'BTC/USD', 60)

        # Verificar resultados
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(last, 'last')


class TestTechnicalIndicators(unittest.TestCase):

    def test_moving_average(self):
        # Crear un DataFrame de prueba
        df = pd.DataFrame({'close': [1, 2, 3, 4, 5]}, index=[datetime.now() for _ in range(5)])
        slot = 3

        # Importar y ejecutar Moving_Average
        from technical_indicators import Moving_Average
        ma = Moving_Average(slot, df)
        result_df = ma.calculate()

        # Verificar resultados
        self.assertIn('moving_average_{}'.format(slot), result_df.columns)

    def test_stochastic_oscillator(self):
        # Crear un DataFrame de prueba
        df = pd.DataFrame({
            'low': [1, 2, 3, 4, 5],
            'high': [5, 4, 3, 2, 1],
            'close': [3, 3, 3, 3, 3]
        }, index=[datetime.now() for _ in range(5)])
        n = 3

        # Importar y ejecutar StochasticOscillator
        from technical_indicators import StochasticOscillator
        so = StochasticOscillator(df, n)
        result_df = so.calculate()

        # Verificar resultados
        self.assertIn('stochastic_osc', result_df.columns)
        self.assertIn('stochastic_osc_ma', result_df.columns)


class TestGraphing(unittest.TestCase):

    def test_graphic(self):
        # Crear un DataFrame de prueba y otros parámetros necesarios
        df = pd.DataFrame({
            'open': [1, 2, 3],
            'close': [2, 3, 4],
            'low': [0, 1, 2],
            'high': [3, 4, 5],
            'stochastic_osc': [20, 30, 40],
            'stochastic_osc_ma': [25, 35, 45],
            'moving_average_10': [2.5, 3.5, 4.5]
        }, index=[datetime.now() for _ in range(3)])
        value_m = [10]
        pair_name = 'BTC/USD'

        # Importar y ejecutar Graph.graphic
        from graphing import Graph
        graph = Graph(df, value_m, pair_name)
        figure = graph.graphic()

        # Verificar que se devuelve una figura de Plotly
        self.assertIn('layout', dir(figure))
        self.assertIn('data', dir(figure))


if __name__ == '__main__':
    unittest.main()