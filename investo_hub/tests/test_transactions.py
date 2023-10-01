from django.test import TestCase
from investo_hub.models import Wallet, Transactions
from investo_hub.transactions import perform_money_transaction, deposit_into_wallet, withdraw_from_wallet, \
    get_or_create_wallet, buy_crypto, get_or_create_cryptos, sell_crypto
from django.contrib.auth.models import User
from decimal import Decimal
from user_management.models import Crypto
from investo_hub.models import Cryptos


class TestPerformMoneyTransaction(TestCase):

    def test_deposit_into_wallet(self):
        # Create a user and a wallet for testing
        user = User.objects.create(username='testuser')
        wallet = Wallet.objects.create(user=user, dollars=0)

        # Call the perform_money_transaction function with a deposit transaction
        perform_money_transaction(user, 100, "deposit")

        # Check if the wallet balance has been updated correctly
        wallet.refresh_from_db()
        self.assertEqual(wallet.dollars, 100)

    def test_withdraw_from_wallet(self):
        # Create a user and a wallet with some balance for testing
        user = User.objects.create(username='testuser')
        wallet = Wallet.objects.create(user=user, dollars=200)

        # Call the perform_money_transaction function with a withdraw transaction
        perform_money_transaction(user, 50, "withdraw")

        # Check if the wallet balance has been updated correctly
        wallet.refresh_from_db()
        self.assertEqual(wallet.dollars, 150)

    def test_invalid_transaction_type(self):
        # Create a user and a wallet for testing
        user = User.objects.create(username='testuser')
        wallet = Wallet.objects.create(user=user, dollars=0)

        # Call the perform_money_transaction function with an invalid transaction type
        with self.assertRaises(ValueError) as context:
            perform_money_transaction(user, 100, "invalid")

        # Check if the function raises a ValueError with the expected message
        self.assertEqual(str(context.exception),
                         "Invalid transaction type. The transaction type must be 'deposit' or 'withdraw'.")


class TestDepositIntoWallet(TestCase):

    def test_valid_deposit(self):
        # Create a user and a wallet for testing
        user = User.objects.create(username='testuser')
        wallet = Wallet.objects.create(user=user, dollars=0)

        # Call the deposit_into_wallet function with a valid deposit amount
        deposit_into_wallet(user, wallet, Decimal('100'))

        # Check if the wallet balance has been updated correctly
        wallet.refresh_from_db()
        self.assertEqual(wallet.dollars, Decimal('100'))

        # Check if a deposit transaction record has been created
        self.assertEqual(
            Transactions.objects.filter(user=user, type="deposit", symbol="dollar", amount=Decimal('100')).count(), 1)

    def test_invalid_deposit(self):
        # Create a user and a wallet for testing
        user = User.objects.create(username='testuser')
        wallet = Wallet.objects.create(user=user, dollars=0)

        # Call the deposit_into_wallet function with a negative deposit amount
        with self.assertRaises(ValueError) as context:
            deposit_into_wallet(user, wallet, Decimal('-1'))

        # Check if the function raises a ValueError with the expected message
        self.assertEqual(str(context.exception),
                         "Unable to deposit. The deposit amount must be greater than or equal to 1.")

        # Check if the wallet balance remains unchanged
        wallet.refresh_from_db()
        self.assertEqual(wallet.dollars, Decimal('0'))


class TestWithdrawFromWallet(TestCase):

    def test_valid_withdrawal(self):
        # Create a user and a wallet with a balance for testing
        user = User.objects.create(username='testuser')
        wallet = Wallet.objects.create(user=user, dollars=Decimal('100'))

        # Call the withdraw_from_wallet function with a valid withdrawal amount
        withdraw_from_wallet(user, wallet, Decimal('50'))

        # Check if the wallet balance has been updated correctly
        wallet.refresh_from_db()
        self.assertEqual(wallet.dollars, Decimal('50'))

        # Check if a withdrawal transaction record has been created
        self.assertEqual(
            Transactions.objects.filter(user=user, type="withdraw", symbol="dollar", amount=Decimal('-50')).count(), 1)

    def test_invalid_withdrawal_amount(self):
        # Create a user and a wallet for testing
        user = User.objects.create(username='testuser')
        wallet = Wallet.objects.create(user=user, dollars=Decimal('100'))

        # Call the withdraw_from_wallet function with an invalid withdrawal amount
        with self.assertRaises(ValueError) as context:
            withdraw_from_wallet(user, wallet, Decimal('-1'))

        # Check if the function raises a ValueError with the expected message
        self.assertEqual(str(context.exception),
                         "Unable to withdraw. The withdrawal amount must be greater than or equal to 1.")

        # Check if the wallet balance remains unchanged
        wallet.refresh_from_db()
        self.assertEqual(wallet.dollars, Decimal('100'))

    def test_insufficient_funds(self):
        # Create a user and a wallet with a balance for testing
        user = User.objects.create(username='testuser')
        wallet = Wallet.objects.create(user=user, dollars=Decimal('50'))

        # Call the withdraw_from_wallet function with an amount exceeding the wallet balance
        with self.assertRaises(ValueError) as context:
            withdraw_from_wallet(user, wallet, Decimal('100'))

        # Check if the function raises a ValueError with the expected message
        self.assertEqual(str(context.exception),
                         "Insufficient funds in your wallet. The withdrawal amount exceeds your available balance.")

        # Check if the wallet balance remains unchanged
        wallet.refresh_from_db()
        self.assertEqual(wallet.dollars, Decimal('50'))


class TestGetOrCreateWallet(TestCase):

    def test_get_existing_wallet(self):
        # Create a user
        user = User.objects.create(username='testuser')

        # Create an existing wallet for the user
        existing_wallet = Wallet.objects.create(user=user)

        # Call the get_or_create_wallet function
        wallet = get_or_create_wallet(user)

        # Check if the returned wallet is the same as the existing wallet
        self.assertEqual(wallet, existing_wallet)

    def test_create_new_wallet(self):
        # Create a user
        user = User.objects.create(username='testuser')

        # Call the get_or_create_wallet function
        wallet = get_or_create_wallet(user)

        # Check if a new wallet has been created for the user
        self.assertIsInstance(wallet, Wallet)

        # Check if the wallet is associated with the correct user
        self.assertEqual(wallet.user, user)


class TestBuyCrypto(TestCase):

    def test_valid_purchase(self):
        # Create a user and a crypto for testing
        user = User.objects.create(username='testuser')
        crypto = Crypto.objects.create(name='bitcoin')
        cryptos = get_or_create_cryptos(user, 'bitcoin')

        # Call the buy_crypto function with a valid purchase amount
        buy_crypto(user, cryptos, Decimal(1))

        # Check if the crypto amount has been updated correctly
        crypto.refresh_from_db()
        self.assertEqual(cryptos.amount, Decimal(1))

        # Check if a buy transaction record has been created
        self.assertEqual(
            Transactions.objects.filter(user=user, type="buy", symbol=cryptos.symbol, amount=Decimal('1')).count(), 1)

    def test_invalid_purchase_amount(self):
        # Create a user and a crypto for testing
        user = User.objects.create(username='testuser')
        crypto = Crypto.objects.create(name='bitcoin')
        cryptos = get_or_create_cryptos(user, 'bitcoin')

        # Call the buy_crypto function with an invalid purchase amount
        with self.assertRaises(ValueError) as context:
            buy_crypto(user, cryptos, Decimal('-1'))

        # Check if the function raises a ValueError with the expected message
        self.assertEqual(str(context.exception), "Unable to buy. The purchase amount must be a positive value.")

        # Check if the crypto amount remains unchanged
        crypto.refresh_from_db()
        self.assertEqual(cryptos.amount, Decimal('0'))


class TestSellCrypto(TestCase):

    def setUp(self):
        # Create a user and a crypto for testing
        self.user = User.objects.create(username='testuser')
        self.crypto = Crypto.objects.create(name='bitcoin')
        self.cryptos = get_or_create_cryptos(self.user, 'bitcoin')
        buy_crypto(self.user, self.cryptos, Decimal(1))

    def test_valid_sell(self):
        # Call the sell_crypto function with a valid purchase amount
        sell_crypto(self.user, self.cryptos, Decimal(1))

        # Check if the crypto amount has been updated correctly
        self.crypto.refresh_from_db()
        self.assertEqual(self.cryptos.amount, Decimal(0))

        # Check if a sell transaction record has been created
        self.assertEqual(
            Transactions.objects.filter(user=self.user, type="buy", symbol=self.cryptos.symbol,
                                        amount=Decimal('1')).count(), 1)

    def test_invalid_sell(self):
        # Call the sell_crypto function with a invalid purchase amount
        with self.assertRaises(ValueError) as context:
            sell_crypto(self.user, self.cryptos, Decimal('-1'))

        # Check if the function raises a ValueError with the expected message
        self.assertEqual(str(context.exception), "Unable to sell. The sell amount must be a positive value.")

        # Check if the crypto amount has not been updated
        self.crypto.refresh_from_db()
        self.assertEqual(self.cryptos.amount, Decimal(1))


class TestGetOrCreateCryptos(TestCase):

    def test_get_existing_cryptos(self):
        # Create a user and a crypto for testing
        user = User.objects.create(username='testuser')
        crypto = Crypto.objects.create(name='bitcoin')
        cryptos = Cryptos.objects.create(user=user, crypto=crypto)

        # Call the get_or_create_cryptos function
        result = get_or_create_cryptos(user, 'bitcoin')

        # Check if the returned cryptos object is the same as the existing one
        self.assertEqual(result, cryptos)

    def test_create_new_cryptos(self):
        # Create a user and a crypto for testing
        user = User.objects.create(username='testuser')
        crypto = Crypto.objects.create(name='bitcoin')

        # Call the get_or_create_cryptos function
        result = get_or_create_cryptos(user, 'bitcoin')

        # Check if a new Cryptos record has been created for the user and crypto
        self.assertIsInstance(result, Cryptos)

        # Check if the created Cryptos record is associated with the correct user and crypto
        self.assertEqual(result.user, user)
        self.assertEqual(result.crypto, crypto)
