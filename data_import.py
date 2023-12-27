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