from investosphere.settings import CRYPTOCURRENCIES
from django.core.cache import cache
from .models import Cryptos
from decimal import Decimal
import requests
import time
import os

COIN_API = os.environ.get('coin_api_url')


def request_coin_api():
    formatted_ids = ", ".join(CRYPTOCURRENCIES)
    params = {
        "vs_currency": "usd",
        "ids": formatted_ids,
        "order": "market_cap_desc",
        "page": 1
    }
    for num in range(5):
        response = requests.get(COIN_API + '/coins/markets', params=params)
        if response.status_code == 200:
            cryptos_cache = response.json()
            cache.set('cached_cryptos_trending', cryptos_cache, 12 * 60 * 60)
            return cryptos_cache
        else:
            time.sleep(5)


def request_coin_cache():
    cryptos_cache = cache.get('cached_cryptos')
    if not cryptos_cache:
        cryptos_cache = request_coin_api()
    return cryptos_cache


def get_coin_info(coin):
    cryptos_cache = request_coin_cache()
    for crypto in cryptos_cache:
        print(coin)
        if crypto['id'] == coin:
            return crypto
    raise Exception(f'Cryptocurrency "{coin}" not found in the cache.')


def get_user_cryptos(user):
    cryptos = Cryptos.objects.filter(user=user)
    for crypto in cryptos:
        crypto.usd = Decimal(get_coin_info(crypto.symbol)['current_price']) * Decimal(crypto.amount)
        crypto.usd = round(crypto.usd, 2)
        crypto.image = get_coin_info(crypto.symbol)['image']
    return cryptos
