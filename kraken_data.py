import krakenex
from pykrakenapi import KrakenAPI

def krakenex_data_import():
    try:
        api = krakenex.API()
        k = KrakenAPI(api)

        data = k.get_tradable_asset_pairs()
        pairs = data['altname'].values.tolist()

        return k, pairs

    except Exception as e:
        print('This problem has occurred with the API: ' + str(e))
def get_ohlc_data(k, pair_name, interval):
    try:
        df, last = k.get_ohlc_data(pair_name, interval=interval)
        return df, last

    except Exception as e:
        print('This problem has occurred while fetching OHLC data: ' + str(e))