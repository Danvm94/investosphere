from django.core.cache import cache
from django.http import JsonResponse
from investosphere import settings
import requests
import os

coin_api_url = os.environ.get('coin_api_url')


def get_top_gainers(per_page):
    cryptos_trending = cache.get('cached_cryptos_trending')
    if not cryptos_trending:
        formatted_ids = ", ".join(settings.CRYPTOCURRENCIES)
        params = {
            "vs_currency": "usd",
            "ids": formatted_ids,
            "order": "market_cap_desc",
            "page": 1
        }
        response = requests.get(coin_api_url + '/coins/markets', params=params)
        if response.status_code == 200:
            cryptos_trending = response.json()
            cache.set('cached_cryptos_trending', cryptos_trending, 45)
    return cryptos_trending[:per_page]


def get_all_coins():
    cryptos_list = settings.CRYPTOCURRENCIES
    return cryptos_list


def get_price(request):
    selected_crypto = request.GET.get('crypto')

    response = requests.get(coin_api_url + f'/coins/{selected_crypto}')

    data = response.json()

    return JsonResponse(data)
