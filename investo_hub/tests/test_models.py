from django.test import TestCase
from investo_hub.models import Wallet, Cryptos, Transactions, Crypto
from django.contrib.auth.models import User


class WalletModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')

    def test_model_creation(self):
        wallet = Wallet.objects.create(user=self.user, dollars=100.50)
        self.assertEqual(wallet.user, self.user)
        self.assertEqual(wallet.dollars, 100.50)
        self.assertIsNotNone(wallet.created_at)

    def test_formatted_amount(self):
        wallet = Wallet.objects.create(user=self.user, dollars=1234.56)
        self.assertEqual(wallet.formatted_amount(), '1,234.56')

    def test_default_value(self):
        wallet = Wallet.objects.create(user=self.user)
        self.assertEqual(wallet.dollars, 0)

    def test_user_relationship(self):
        wallet = Wallet.objects.create(user=self.user, dollars=50.25)
        self.assertEqual(wallet.user, self.user)


class CryptosModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.crypto = Crypto.objects.create(name="bitcoin")

    def test_model_creation(self):
        cryptos = Cryptos.objects.create(user=self.user, crypto=self.crypto,
                                         amount=0)
        self.assertEqual(cryptos.user, self.user)
        self.assertEqual(cryptos.crypto, self.crypto)
        self.assertEqual(cryptos.amount, 0)

    def test_formatted_amount(self):
        cryptos = Cryptos.objects.create(user=self.user, crypto=self.crypto,
                                         amount=0.500000)
        self.assertEqual(cryptos.formatted_amount(), '0.5')

    def test_default_value(self):
        cryptos = Cryptos.objects.create(user=self.user, crypto=self.crypto)
        self.assertEqual(cryptos.amount, 0)

    def test_user_relationship(self):
        cryptos = Cryptos.objects.create(user=self.user, crypto=self.crypto)
        self.assertEqual(cryptos.user, self.user)

    def test_symbol_value(self):
        cryptos = Cryptos.objects.create(user=self.user, crypto=self.crypto)
        self.assertEqual(cryptos.symbol, self.crypto.name)


class TransactionsModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.crypto = Crypto.objects.create(name="bitcoin")
        self.cryptos = Cryptos.objects.create(user=self.user,
                                              crypto=self.crypto,
                                              amount=0.500000)

    def test_model_creation_usd(self):
        transactions = Transactions.objects.create(user=self.user,
                                                   type='deposit',
                                                   symbol='dollar', amount=50)
        self.assertEqual(transactions.user, self.user)
        self.assertEqual(transactions.type, 'deposit')
        self.assertEqual(transactions.symbol, 'dollar')
        self.assertEqual(transactions.amount, 50)

    def test_model_creation_crypto(self):
        transactions = Transactions.objects.create(user=self.user,
                                                   type='deposit',
                                                   symbol=self.cryptos.symbol,
                                                   amount=0.60)
        self.assertEqual(transactions.user, self.user)
        self.assertEqual(transactions.type, 'deposit')
        self.assertEqual(transactions.symbol, self.cryptos.symbol)
        self.assertEqual(transactions.amount, 0.60)
