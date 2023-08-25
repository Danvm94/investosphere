def perform_money_transaction(user, amount, transaction):
    wallet = get_or_create_wallet(user)
    if transaction == "deposit":
        deposit_into_wallet(user, wallet, amount)
    elif transaction == "withdraw":
        withdraw_from_wallet(user, wallet, amount)
    wallet.save()


def deposit_into_wallet(user, wallet, amount):
    if amount < 1:
        raise ValueError(
            "Unable to deposit. "
            "The deposit amount must be greater than or equal to 1.")
    else:
        wallet.dollars += amount
        transaction = Transactions.objects.create(
            user=user,  type="deposit", symbol="dollar", amount=amount)


def withdraw_from_wallet(user, wallet, amount):
    if amount <= 1:
        raise ValueError(
            "Unable to withdraw. "
            "The withdrawal amount must be greater than or equal to 1.")
    elif wallet.dollars < amount:
        raise ValueError(
            "Insufficient funds in your wallet. "
            "The withdrawal amount exceeds your available balance.")
    else:
        wallet.dollars -= amount
        transaction = Transactions.objects.create(
            user=user,  type="withdraw", symbol="dollar", amount=-amount)


def get_or_create_wallet(user):
    try:
        wallet = Wallet.objects.get(user=user)
    except Wallet.DoesNotExist:
        wallet = Wallet.objects.create(user=user)
    return wallet
