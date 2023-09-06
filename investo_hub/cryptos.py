from investosphere.settings import CRYPTOCURRENCIES
from django.core.cache import cache
from .models import Cryptos
from decimal import Decimal
import requests
import time
import datetime
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
            cache.set('cached_cryptos', cryptos_cache, 1 * 60 * 60)
            return cryptos_cache
        else:
            time.sleep(5)


def request_coin_api_chart():
    cryptos_cache = cache.get('cached_cryptos')
    cryptos_market_chart = []
    current_time = datetime.datetime.now()
    target_time = current_time.replace(hour=1, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
    time_difference_seconds = (target_time - current_time).total_seconds()

    for crypto in cryptos_cache:
        params = {
            "vs_currency": 'usd',
            "days": '30',
            'interval': 'daily'
        }
        crypto_id = crypto['id']
        for num in range(5):
            response = requests.get(COIN_API + f'/coins/{crypto_id}/market_chart', params=params)
            if response.status_code == 200:
                prices = response.json()['prices']
                cryptos_market_chart.append({crypto['id']: prices})
                break
            else:
                print('got here, waiting 5 seconds')
                time.sleep(5)
    organized_data = {}
    for entry in cryptos_market_chart:
        for crypto_name, crypto_data in entry.items():
            organized_data[crypto_name] = {
                'timestamps': [],
                'values': []
            }
            for timestamp, value in crypto_data:
                organized_data[crypto_name]['timestamps'].append(timestamp)
                organized_data[crypto_name]['values'].append(value)
    cache.set('cached_cryptos_char', organized_data, 1 * 60 * 60)
    return organized_data


def request_coin_chart_cache():
    cached_cryptos_chart = cache.get('cached_cryptos_char')
    if not cached_cryptos_chart:
        cached_cryptos_chart = request_coin_api_chart()
    return cached_cryptos_chart


def request_coin_cache():
    cryptos_cache = cache.get('cached_cryptos')
    if not cryptos_cache:
        cryptos_cache = request_coin_api()
    return cryptos_cache


def get_coin_info(coin):
    cryptos_cache = request_coin_cache()
    for crypto in cryptos_cache:
        if crypto['id'] == coin:
            return crypto
    raise Exception(f'Cryptocurrency "{coin}" not found in the cache.')


def get_user_cryptos(user):
    cryptos = Cryptos.objects.filter(user=user)
    for crypto in cryptos:
        print(crypto.symbol)
        crypto.usd = Decimal(get_coin_info(crypto.symbol)['current_price']) * Decimal(crypto.amount)
        crypto.usd = round(crypto.usd, 2)
        crypto.image = get_coin_info(crypto.symbol)['image']
    return cryptos
