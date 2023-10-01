from django.test import TestCase
from investo_hub.forms import TransactionsViewForm, CryptoTransactionsViewForm, DepositMoneyForm, WithdrawMoneyForm, \
    BuyCryptoForm, SellCryptoForm
from datetime import date, timedelta
from user_management.models import Crypto
from investo_hub.models import Cryptos
from django.contrib.auth.models import User


class TransactionsViewFormTestCase(TestCase):
    def test_form_fields(self):
        form = TransactionsViewForm()

        # Check if the form has the expected fields
        self.assertIn('transaction_type', form.fields)
        self.assertIn('start_date', form.fields)
        self.assertIn('end_date', form.fields)

    def test_form_initial_values(self):
        form = TransactionsViewForm()

        # Check the initial values of the form fields
        self.assertEqual(form.fields['transaction_type'].initial, 'all')
        self.assertEqual(form.fields['start_date'].initial, date.today() - timedelta(days=30))
        self.assertEqual(form.fields['end_date'].initial, date.today() + timedelta(days=1))

    def test_valid_form_data(self):
        # Create a dictionary of valid form data
        form_data = {
            'transaction_type': 'deposit',
            'start_date': '2023-09-01',
            'end_date': '2023-09-15',
        }
        form = TransactionsViewForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_form_data(self):
        # Create a dictionary of invalid form data
        form_data = {
            'transaction_type': 'invalid_type',
            'start_date': '2023-09-01',
            'end_date': '2023-09-15',
        }
        form = TransactionsViewForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())


class CryptoTransactionsViewFormTestCase(TestCase):
    def test_valid_crypto_choice(self):
        # Create a dictionary of valid form data
        form_data = {
            'transaction_type': 'buy',
            'start_date': '2023-09-01',
            'end_date': '2023-09-15',
        }
        form = CryptoTransactionsViewForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_crypto_choice(self):
        # Create a dictionary of invalid form data
        form_data = {
            'transaction_type': 'buy',
            'start_date': '2023-09-01',
            'end_date': '2023-09-15',
            'crypto_choice': 'nonexistent_crypto',
        }
        form = CryptoTransactionsViewForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        self.assertIn('crypto_choice', form.errors)


class DepositMoneyFormTestCase(TestCase):
    def test_valid_deposit_amount(self):
        # Create a dictionary of valid form data
        form_data = {
            'deposit_dollars': '100.00',  # A valid deposit amount within the range
        }
        form = DepositMoneyForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_deposit_amount_less_than_minimum(self):
        # Create a dictionary of invalid form data (less than the minimum)
        form_data = {
            'deposit_dollars': '0.50',  # An amount less than the minimum allowed ($1.00)
        }
        form = DepositMoneyForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        self.assertIn('deposit_dollars', form.errors)  # Check for the 'deposit_dollars' field error

    def test_invalid_deposit_amount_exceeds_maximum(self):
        # Create a dictionary of invalid form data (exceeds the maximum)
        form_data = {
            'deposit_dollars': '60000.00',  # An amount exceeding the maximum allowed ($50,000.00)
        }
        form = DepositMoneyForm(data=form_data)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        self.assertIn('deposit_dollars', form.errors)


class WithdrawMoneyFormTestCase(TestCase):
    def test_valid_withdraw_amount(self):
        # Create a dictionary of valid form data
        form_data = {
            'withdraw_dollars': '100.00',  # A valid withdraw amount within the range
        }
        max_value = 1000.00  # Set the maximum value for testing
        form = WithdrawMoneyForm(data=form_data, max_value=max_value)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_withdraw_amount_less_than_minimum(self):
        # Create a dictionary of invalid form data (less than the minimum)
        form_data = {
            'withdraw_dollars': '0.50',  # An amount less than the minimum allowed ($1.00)
        }
        max_value = 1000.00  # Set the maximum value for testing
        form = WithdrawMoneyForm(data=form_data, max_value=max_value)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        self.assertIn('withdraw_dollars', form.errors)  # Check for the 'withdraw_dollars' field error

    def test_invalid_withdraw_amount_exceeds_maximum(self):
        # Create a dictionary of invalid form data (exceeds the maximum)
        form_data = {
            'withdraw_dollars': '2000.00',  # An amount exceeding the maximum allowed ($1000.00)
        }
        max_value = 1000.00  # Set the maximum value for testing
        form = WithdrawMoneyForm(data=form_data, max_value=max_value)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        self.assertIn('withdraw_dollars', form.errors)  # Check for the 'withdraw_dollars' field error

    class BuyCryptoFormTestCase(TestCase):
        def test_valid_form_data(self):
            # Create a dictionary of valid form data
            form_data = {
                'crypto_select': 'bitcoin',
                'buy_dollars': '100.00',  # A valid USD amount
            }
            max_value = 1000.00  # Set the maximum value for testing
            form = BuyCryptoForm(data=form_data, max_value=max_value)

            # Check if the form is valid
            self.assertTrue(form.is_valid())

        def test_invalid_usd_amount_less_than_minimum(self):
            # Create a dictionary of invalid form data (USD amount less than the minimum)
            form_data = {
                'crypto_select': 'bitcoin',
                'buy_dollars': '0.50',  # An amount less than the minimum allowed ($1.00)
            }
            max_value = 1000.00  # Set the maximum value for testing
            form = BuyCryptoForm(data=form_data, max_value=max_value)

            # Check if the form is invalid
            self.assertFalse(form.is_valid())
            self.assertIn('buy_dollars', form.errors)  # Check for the 'buy_dollars' field error

        def test_invalid_usd_amount_exceeds_maximum(self):
            # Create a dictionary of invalid form data (USD amount exceeds the maximum)
            form_data = {
                'crypto_select': 'bitcoin',
                'buy_dollars': '2000.00',  # An amount exceeding the maximum allowed ($1000.00)
            }
            max_value = 1000.00  # Set the maximum value for testing
            form = BuyCryptoForm(data=form_data, max_value=max_value)

            # Check if the form is invalid
            self.assertFalse(form.is_valid())
            self.assertIn('buy_dollars', form.errors)  # Check for the 'buy_dollars' field error


class SellCryptoFormTestCase(TestCase):
    def setUp(self):
        # Create a list of available cryptocurrencies for testing
        self.ethereum = Crypto.objects.create(name='ethereum')  # Create instances with amount
        self.bitcoin = Crypto.objects.create(name='bitcoin')  # Create instances with amount
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.cryptos_btc = Cryptos.objects.create(user=self.user, crypto=self.bitcoin, amount=10)
        self.cryptos_eth = Cryptos.objects.create(user=self.user, crypto=self.ethereum, amount=10)
        self.cryptocurrencies = [self.cryptos_btc, self.cryptos_eth]  # Use model instances

    def test_valid_form_data(self):
        # Create a dictionary of valid form data
        form_data = {
            'crypto_select': 'bitcoin',
            'sell_cryptos': '5.0',  # A valid amount less than the available balance
        }
        form = SellCryptoForm(data=form_data, cryptocurrencies=self.cryptocurrencies)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_sell_amount_exceeds_balance(self):
        # Create a dictionary of invalid form data (sell amount exceeds the available balance)
        form_data = {
            'crypto_select': 'bitcoin',
            'sell_cryptos': '15.0',  # An amount exceeding the available balance (10.0)
        }
        form = SellCryptoForm(data=form_data, cryptocurrencies=self.cryptocurrencies)

        # Check if the form is invalid
        self.assertFalse(form.is_valid())
