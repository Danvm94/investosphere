from .models import Wallet, Transactions, Cryptos
# from .cryptos import


def perform_money_transaction(user, amount, transaction):
    wallet = get_or_create_wallet(user)
    if transaction == "deposit":
        deposit_into_wallet(user, wallet, amount)
    elif transaction == "withdraw":
        withdraw_from_wallet(user, wallet, amount)
    else:
        raise ValueError("Invalid transaction type. The transaction type must be 'deposit' or 'withdraw'.")
    wallet.save()


def deposit_into_wallet(user, wallet, amount):
    """
    Deposit an amount into the user's wallet.

    This function adds the specified amount to the user's wallet balance through a deposit.

    Args:
        user (User): The user for whom the deposit is made.
        wallet (Wallet): The user's wallet object.
        amount (Decimal): The amount to be deposited.

    Raises:
        ValueError: If the deposit amount is less than 1.

    Returns:
        None
    """
    if amount < 0:
        raise ValueError(
            "Unable to deposit. "
            "The deposit amount must be greater than or equal to 1.")
    else:
        wallet.dollars += amount
        Transactions.objects.create(user=user,  type="deposit", symbol="dollar", amount=amount)


def withdraw_from_wallet(user, wallet, amount):
    """
    Withdraw an amount from the user's wallet.

    This function deducts the specified amount from the user's wallet balance through a withdrawal.

    Args:
        user (User): The user for whom the withdrawal is made.
        wallet (Wallet): The user's wallet object.
        amount (Decimal): The amount to be withdrawn.

    Raises:
        ValueError: If the withdrawal amount is less than or equal to 1
                    or if the user's wallet balance is insufficient.

    Returns:
        None
    """
    if amount < 0:
        raise ValueError(
            "Unable to withdraw. "
            "The withdrawal amount must be greater than or equal to 1.")
    elif wallet.dollars < amount:
        raise ValueError(
            "Insufficient funds in your wallet. "
            "The withdrawal amount exceeds your available balance.")
    else:
        wallet.dollars -= amount
        Transactions.objects.create(user=user,  type="withdraw", symbol="dollar", amount=-amount)


def get_or_create_wallet(user):
    """
   Get or create a wallet for the specified user.

   This function retrieves an existing wallet associated with the user or creates a new one
   if a wallet does not already exist.

   Args:
       user (User): The user for whom the wallet is retrieved or created.

   Returns:
       Wallet: The wallet associated with the user.
    """
    try:
        wallet = Wallet.objects.get(user=user)
    except Wallet.DoesNotExist:
        wallet = Wallet.objects.create(user=user)
    return wallet


def perform_crypto_transaction(user, crypto, amount, transaction):
    cryptos = get_or_create_cryptos(user, crypto)
    if transaction == 'buy':
        buy_crypto(user, cryptos, amount)
    elif transaction == 'sell':
        sell_crypto(user, cryptos, amount)


def buy_crypto(user, crypto, amount):
    if amount < 0:
        raise ValueError(
            "Unable to buy. "
            "The purchase amount must be a positive value."
        )
    else:
        crypto.amount += amount
        crypto.save()


def sell_crypto(user, crypto, amount):
    if amount < 0:
        raise ValueError(
            "Unable to sell. "
            "The sell amount must be a positive value."
        )
    elif amount > crypto.amount:
        raise ValueError(
            "Unable to sell. "
            "insufficient."
        )
    else:
        crypto.amount -= amount
        crypto.save()
    pass


def get_or_create_cryptos(user, symbol):
    try:
        cryptos = Cryptos.objects.get(user=user, symbol=symbol)
    except Cryptos.DoesNotExist:
        cryptos = Cryptos.objects.create(user=user, symbol=symbol)
    return cryptos
