from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .models import Wallet, Transactions
from .forms import TransactionsViewForm, DepositMoneyForm, WithdrawMoneyForm, BuyCryptoForm, SellCryptoForm, \
    CryptoTransactionsViewForm
from .transactions import perform_money_transaction, perform_crypto_transaction
from .cryptos import get_coin_info, get_user_cryptos
from .portfolios import get_all_portfolios
from django.http import JsonResponse
import random


def chart_view(request):
    labels = ["January", "February", "March", "April", "May"]
    data = [random.randint(1, 10) for _ in range(5)]

    return render(request, 'chart.html', {'labels': labels, 'data': data})


@login_required
def wallet_view(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    deposit_money_form = DepositMoneyForm(request.POST or None)
    withdraw_money_form = WithdrawMoneyForm(request.POST or None, max_value=wallet.dollars)
    transactions_view_form = TransactionsViewForm(request.GET or None)
    if request.method == 'POST':
        if deposit_money_form.is_valid():
            amount = deposit_money_form.cleaned_data['deposit_dollars']
            print(amount)
            try:
                perform_money_transaction(user, amount, 'deposit')
            except ValueError as error:
                messages.warning(request, error)
        if withdraw_money_form.is_valid():
            amount = withdraw_money_form.cleaned_data['withdraw_dollars']
            print(amount)
            try:
                perform_money_transaction(user, amount, 'withdraw')
            except ValueError as error:
                messages.warning(request, error)
        return redirect('wallet')

    elif request.method == 'GET':
        if transactions_view_form.is_valid():
            start_date = transactions_view_form.cleaned_data['start_date']
            end_date = transactions_view_form.cleaned_data['end_date']
            transaction_type = transactions_view_form.cleaned_data['transaction_type']
            filter_args = {
                'user': user,
                'symbol': 'dollar',
                'created_at__range': (start_date, end_date),
            }
            if transaction_type != 'all':
                print(transaction_type)
                filter_args['type'] = transaction_type
            transactions = Transactions.objects.filter(**filter_args).order_by('-created_at')
        else:
            transactions = Transactions.objects.filter(user=user, symbol="dollar").order_by('-created_at')
        return render(request, 'wallet.html',
                      {'transactions': transactions, 'deposit_money_form': deposit_money_form,
                       'withdraw_money_form': withdraw_money_form, 'wallet': wallet,
                       'transactions_view_form': transactions_view_form})


@login_required
def crypto_view(request):
    user = request.user
    buy_crypto_form = BuyCryptoForm(request.POST or None)
    sell_crypto_form = SellCryptoForm(request.POST or None, cryptocurrencies=get_user_cryptos(user))
    transactions_view_form = CryptoTransactionsViewForm(request.GET or None)
    if request.method == 'POST':
        if buy_crypto_form.is_valid():
            usd_amount = buy_crypto_form.cleaned_data['buy_dollars_decimal']
            crypto = buy_crypto_form.cleaned_data['crypto_select']
            crypto_price = Decimal(get_coin_info(crypto)['current_price'])
            crypto_amount = usd_amount / crypto_price
            perform_money_transaction(user, usd_amount, 'withdraw')
            perform_crypto_transaction(user, crypto, crypto_amount, 'buy')
        if sell_crypto_form.is_valid():
            crypto_amount = Decimal(sell_crypto_form.cleaned_data['sell_cryptos'])
            print(f'crypto_amount: {crypto_amount}')
            crypto = sell_crypto_form.cleaned_data['crypto_select']
            print(f'crypto: {crypto}')
            crypto_price = Decimal(get_coin_info(crypto)['current_price'])
            print(f'crypto_price: {crypto_price}')
            crypto_price_decimal = Decimal(crypto_price)
            print(f'crypto_price_decimal: {crypto_price_decimal}')
            usd_amount = crypto_amount * crypto_price_decimal
            print(f'usd_amount: {usd_amount}')
            perform_crypto_transaction(user, crypto, crypto_amount, 'sell')
            perform_money_transaction(user, usd_amount, 'deposit')
        return redirect('crypto')

    elif request.method == 'GET':
        user_cryptos = get_user_cryptos(user)

        wallet = Wallet.objects.get(user=user)
        balance = wallet.dollars
        if transactions_view_form.is_valid():
            start_date = transactions_view_form.cleaned_data['start_date']
            end_date = transactions_view_form.cleaned_data['end_date']
            transaction_type = transactions_view_form.cleaned_data['transaction_type']
            crypto = transactions_view_form.cleaned_data['crypto_choice']
            filter_args = {
                'user': user,
                'created_at__range': (start_date, end_date),
            }
            if transaction_type != 'all':
                print(transaction_type)
                filter_args['type'] = transaction_type
            if crypto != 'all':
                filter_args['symbol'] = crypto

            transactions = Transactions.objects.filter(**filter_args).exclude(symbol='dollar').order_by('-created_at')
        else:
            transactions = Transactions.objects.filter(user=user).exclude(symbol='dollar').order_by('-created_at')
        return render(request, 'crypto.html',
                      {'buy_crypto_form': buy_crypto_form, 'sell_crypto_form': sell_crypto_form,
                       'user_cryptos': user_cryptos, 'transactions': transactions,
                       'balance': balance, 'transactions_view_form': transactions_view_form})


def get_price_view(request):
    crypto_selected = request.GET.get('crypto', None)
    if crypto_selected:
        crypto_info = get_coin_info(crypto_selected)
        return JsonResponse(crypto_info)
