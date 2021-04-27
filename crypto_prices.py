import cryptocompare as cc
from pprint import pprint
import coinmarketcapapi
from datetime import datetime

def get_crypto_info(args):
    currency = 'USD'
    crypto_symbol = 'btc'
    crypto_name = 'bitcoin'
    # pprint(cc.get_coin_list())

    #TODO rozpoznawanie nazwy/symbolu z mowy

    # cmc = coinmarketcapapi.CoinMarketCapAPI('3a9b4f7c-ca5b-4899-a76d-49cbef569178') #todo w gotowej wersji mozna przez api key
    cmc = coinmarketcapapi.CoinMarketCapAPI() # TODO nie wiem jak inaczej zdobyc symbol z nazwy

    q = cmc.cryptocurrency_info(symbol=crypto_symbol)
    q = cmc.cryptocurrency_info(slug=crypto_name)

    for _, info in q.data.items():
        # pprint(info)
        symbol, name = info['name'], info['symbol']


    pprint(cc.get_price(name, currency))
    pprint(cc.get_avg(name, currency))

    pprint(cc.get_historical_price(name, currency, datetime(2019, 11, 3)))





if __name__ == '__main__':
    get_crypto_info(None)

