from django.core.cache import cache
from django.http import JsonResponse
from investosphere import settings
from decimal import Decimal
from .models import Cryptos
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


def get_coin_info(request):
    selected_crypto = request.GET.get('crypto')
    response = requests.get(coin_api_url + f'/coins/{selected_crypto}')
    data = response.json()
    return JsonResponse(data)


def get_coin_price(coin):
    response = requests.get(coin_api_url + f'/coins/{coin}')
    data = response.json()
    price = data["market_data"]["current_price"]["usd"]
    return price


def get_user_crypto(user, symbol):
    try:
        crypto = Cryptos.objects.get(user=user, symbol=symbol)
    except Cryptos.DoesNotExist:
        crypto = Cryptos.objects.create(user=user, symbol=symbol, amount=0)
    return crypto


def add_user_crypto(user, symbol, amount):
    crypto = get_user_crypto(user, symbol)
    crypto.amount += amount
    print(amount)
    print(type(amount))
    crypto.save()


def get_user_cryptos(user):
    cryptos = Cryptos.objects.filter(user=user)
    for crypto in cryptos:
        crypto.usd = Decimal(get_coin_price(crypto.symbol)) * Decimal(crypto.amount)

    return cryptos


def remove_user_crypto(user, symbol, amount):
    crypto = get_user_crypto(user, symbol)
    if amount <= 1:
        raise ValueError(
            "Unable to withdraw. "
            "The withdrawal amount must be greater than or equal to 1.")
    elif crypto.amount < amount:
        raise ValueError(
            "Insufficient funds in your crypto wallet. "
            "The sell amount exceeds your available balance.")
    else:
        crypto.amount -= amount
        crypto.save()


def get_total_usd_cryptos(user_cryptos):
    total_usd = 0
    for user_crypto in user_cryptos:
        total_usd += user_crypto.usd
    return total_usd
