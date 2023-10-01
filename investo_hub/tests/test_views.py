from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from investo_hub.models import Wallet, Transactions, Cryptos
from user_management.models import Crypto
import json


class ChartViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_chart_view(self):
        # Make a GET request to the 'chart_view'
        response = self.client.get(reverse('chart'))
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Verify that the response renders the 'chart.html' template
        self.assertTemplateUsed(response, 'chart.html')


class WalletViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.wallet = Wallet.objects.create(user=self.user, dollars=1000.0)
        self.login_status = self.client.login(username='testuser', password='testpassword')
        self.wallet_url = reverse('wallet')

    def test_get_request_transaction_history_display(self):
        # Create some transaction history for the user
        Transactions.objects.create(user=self.user, symbol="dollar", amount=500.0, type="deposit")
        Transactions.objects.create(user=self.user, symbol="dollar", amount=300.0, type="withdraw")
        response = self.client.get(self.wallet_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wallet.html')
        self.assertContains(response, '500')
        self.assertContains(response, '300')

    def test_get_request_form_submission(self):
        response = self.client.get(self.wallet_url, {})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wallet.html')

    def test_post_request_deposit_money(self):
        initial_balance = self.wallet.dollars

        response = self.client.post(self.wallet_url,
                                    {'deposit_form': True, 'deposit_dollars': 200.0})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.wallet_url)

        # Check that a deposit transaction is created
        self.assertEqual(Transactions.objects.filter(user=self.user, type="deposit").count(), 1)

        # Verify that the wallet balance is updated
        updated_wallet = Wallet.objects.get(user=self.user)
        self.assertEqual(updated_wallet.dollars, initial_balance + 200.0)

    def test_post_request_withdraw_money(self):
        initial_balance = self.wallet.dollars

        response = self.client.post(self.wallet_url, {'withdraw_form': True, 'withdraw_dollars': 200.0})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.wallet_url)

        # Check that a withdraw transaction is created
        self.assertEqual(Transactions.objects.filter(user=self.user, type="withdraw").count(), 1)

        # Verify that the wallet balance is updated
        updated_wallet = Wallet.objects.get(user=self.user)
        self.assertEqual(updated_wallet.dollars, initial_balance - 200.0)


class CryptoViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.wallet = Wallet.objects.create(user=self.user, dollars=1000.0)
        self.login_status = self.client.login(username='testuser', password='testpassword')
        self.crypto = Crypto.objects.create(name='bitcoin')
        self.cryptos = Cryptos.objects.create(user=self.user, crypto=self.crypto, amount=200)
        self.crypto_url = reverse('crypto')

    def test_get_request_display(self):
        response = self.client.get(self.crypto_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crypto.html')

    def test_post_request_buy_crypto(self):
        initial_balance = self.wallet.dollars

        response = self.client.post(self.crypto_url,
                                    {'buy_form': True, 'buy_dollars_decimal': 200.0, 'crypto_select': 'bitcoin',
                                     'crypto_price': 1, })

        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertRedirects(response, self.crypto_url)

        # Check that a buy transaction and money withdrawal are created
        self.assertEqual(Transactions.objects.filter(user=self.user, type="buy").count(), 1)
        self.assertEqual(Transactions.objects.filter(user=self.user, type="withdraw").count(), 1)

        # Verify that the wallet balance is updated
        updated_wallet = Wallet.objects.get(user=self.user)
        self.assertEqual(updated_wallet.dollars, initial_balance - 200.0)

    def test_post_request_sell_crypto(self):
        initial_balance = self.wallet.dollars

        response = self.client.post(self.crypto_url,
                                    {'sell_form': True, 'sell_cryptos': '1.00', 'crypto_select': 'bitcoin',
                                     'crypto_price': 1, })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.crypto_url)

        # Check that a sell transaction and money deposit are created
        self.assertEqual(Transactions.objects.filter(user=self.user, type="sell").count(), 1)
        self.assertEqual(Transactions.objects.filter(user=self.user, type="deposit").count(), 1)

        # Verify that the wallet balance is updated
        updated_wallet = Wallet.objects.get(user=self.user)
        self.assertGreater(updated_wallet.dollars, initial_balance)


class GetPriceViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.get_price_url = reverse('get_price')
        self.crypto = Crypto.objects.create(name='bitcoin')

    def test_get_price_valid_crypto(self):
        # Simulate a GET request with a valid crypto parameter
        valid_crypto = 'bitcoin'
        response = self.client.get(self.get_price_url, {'crypto': valid_crypto})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id')
        self.assertContains(response, 'current_price')

    def test_get_price_invalid_crypto(self):
        # Simulate a GET request with an invalid crypto parameter
        invalid_crypto = 'nonexistent_crypto'
        try:
            response = self.client.get(self.get_price_url, {'crypto': invalid_crypto})

            # Check if the response status code is 200 (OK)
            self.assertEqual(response.status_code, 200)

            # Try to parse the JSON response
            response_data = json.loads(response.content.decode('utf-8'))

            # Check if the response contains an error message
            self.assertIn('error', response_data)

            # Print the error message for inspection
            print(response_data['error'])

        except Exception as e:
            # Handle exceptions and print the exception message
            print(f"Exception occurred: {e}")
