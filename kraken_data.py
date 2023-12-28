# Importar la biblioteca krakenex y pykrakenapi
import krakenex
from pykrakenapi import KrakenAPI

# Definición de la función para importar datos desde Kraken
def krakenex_data_import():
    try:
        # Inicializar el API de Krakenex
        api = krakenex.API()

        # Crear un objeto KrakenAPI a partir de la API de Krakenex
        k = KrakenAPI(api)

        # Obtener los pares de activos negociables de Kraken
        data = k.get_tradable_asset_pairs()

        # Extraer los nombres alternativos de los pares de activos y convertirlos a una lista
        pairs = data['altname'].values.tolist()

        # Devolver el objeto KrakenAPI y la lista de pares de activos
        return k, pairs

    # Capturar cualquier excepción que ocurra durante la ejecución
    except Exception as e:
        # Imprimir el error si ocurre alguno relacionado con la API
        print('This problem has occurred with the API: ' + str(e))

# Definición de la función para obtener datos OHLC (Open, High, Low, Close)
def get_ohlc_data(k, pair_name, interval):
    try:
        # Usar la API para obtener datos OHLC para un par específico en un intervalo dado
        df, last = k.get_ohlc_data(pair_name, interval=interval)

        # Devolver el dataframe con los datos OHLC y el último valor
        return df, last

    # Capturar cualquier excepción que ocurra durante la obtención de los datos OHLC
    except Exception as e:
        # Imprimir el error si ocurre alguno al obtener los datos OHLC
        print('This problem has occurred while fetching OHLC data: ' + str(e))
