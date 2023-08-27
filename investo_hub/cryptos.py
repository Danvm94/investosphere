from django.core.cache import cache
import requests
import os

coin_api_url = os.environ.get('coin_api_url')


def get_top_gainers(per_page):
    cryptos_trending = cache.get('cached_cryptos_trending')
    if not cryptos_trending:
        print("here")
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": per_page,
            "page": 1
        }
        response = requests.get(coin_api_url + '/coins/markets', params=params)
        if response.status_code == 200:
            cryptos_trending = response.json()
            cache.set('cached_cryptos_trending', cryptos_trending, 24 * 60 * 60)
    return cryptos_trending
