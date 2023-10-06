from django.test import TestCase
from investo_hub.models import Crypto
from investo_hub.cryptos import get_all_cryptos_names


class TestGetAllCryptosNames(TestCase):

    def test_get_cryptos_names(self):
        # Create some cryptocurrencies for testing
        Crypto.objects.create(name='bitcoin')
        Crypto.objects.create(name='ethereum')
        Crypto.objects.create(name='litecoin')

        # Call the get_all_cryptos_names function
        result = get_all_cryptos_names()

        # Check if the function returns a list of cryptocurrency names
        self.assertListEqual(result, ['bitcoin', 'ethereum', 'litecoin'])

    def test_no_cryptos(self):
        # Call the get_all_cryptos_names function when there
        # are no cryptocurrencies
        result = get_all_cryptos_names()

        # Check if the function returns False
        self.assertFalse(result)
