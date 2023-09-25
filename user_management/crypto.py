from .models import Crypto


def get_all_cryptos_names():
    cryptos = Crypto.objects.all()
    crypto_names = [crypto.name for crypto in cryptos]
    return crypto_names