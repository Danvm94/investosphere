from django.core.cache import cache
from django.http import JsonResponse
import requests
import os

coin_api_url = os.environ.get('coin_api_url')


def get_top_gainers(per_page):
    cryptos_trending = cache.get('cached_cryptos_trending')[:per_page]
    if not cryptos_trending:
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


def get_all_coins():
    cryptos_list = cache.get('cached_cryptos_list')
    if not cryptos_list:
        response = requests.get(coin_api_url + '/coins/list')
        if response.status_code == 200:
            cryptos_list = response.json()
            cache.set('cached_cryptos_trending', cryptos_list, 24 * 60 * 60)
    return cryptos_list


def get_price(request):
    selected_crypto = request.GET.get('crypto')
    print(f"Here {selected_crypto}")
    response = requests.get(coin_api_url + f'/coins/{selected_crypto}')
    print(response.status_code)
    data = response.json()
    print(data)
    return JsonResponse(data)
