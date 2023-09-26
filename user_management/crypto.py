from .models import Crypto


def get_all_cryptos_names():
    if Crypto:
        cryptos = Crypto.objects.all()
        crypto_names = [crypto.name for crypto in cryptos]
    else:
        crypto_names = False
    return crypto_names
