import cryptocompare as cc
from pprint import pprint
import coinmarketcapapi
from datetime import datetime
from recognition_engine import Recognition_engine


def get_crypto_info(args):
    currency = 'USD'
    if len(args) < 1:
        args = Recognition_engine().get_transcript(text="tell me what crypto are you interested in?")

    crypto = args[0].upper() + args[1:]
    print(crypto)
    cmc = coinmarketcapapi.CoinMarketCapAPI('3a9b4f7c-ca5b-4899-a76d-49cbef569178')  # todo w gotowej wersji klucz
    # cmc = coinmarketcapapi.CoinMarketCapAPI('c54bcf4d-1bca-4e8e-9a24-22ff2c3d462b', sandbox=True)

    q = None
    try:
        q = cmc.cryptocurrency_info(symbol=crypto.upper())
    except:
        try:
            q = cmc.cryptocurrency_info(slug=crypto.lower())
        except:
            pass

    if q is None:
        return None

    for _, info in q.data.items():
        # pprint(info)
        name, symbol = info['name'], info['symbol']

    # pprint(cc.get_price(symbol, currency))
    try:
        price_dict = cc.get_avg(symbol, currency)
        pprint(price_dict)
    except:
        price_dict = None

    if price_dict is None:
        return None
    return "price of {symbol} is {price} {currency}".format(symbol=symbol, price=price_dict['PRICE'], currency=currency)


if __name__ == '__main__':
    print(get_crypto_info("cardano"))
    print(get_crypto_info("ADA"))
