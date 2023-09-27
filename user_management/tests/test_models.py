from django.test import TestCase
from investo_hub.models import Crypto


class CryptoModelTestCase(TestCase):
    def test_model_creation(self):
        crypto = Crypto.objects.create(name='bitcoin')
        self.assertEqual(crypto.name, 'bitcoin')
