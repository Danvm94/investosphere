from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .models import Wallet, Portfolio, Transactions
from .forms import PortfolioForm, ManageMoneyForm, BuyCryptoForm, SellCryptoForm
from .transactions import perform_money_transaction, perform_crypto_transaction
from .cryptos import get_top_gainers, get_all_coins, get_coin_info, get_coin_price, add_user_crypto, get_user_cryptos, \
    remove_user_crypto, get_total_usd_cryptos
from .portfolios import get_all_portfolios


@login_required
def portfolio_view(request):
    user = request.user
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        portfolios = get_all_portfolios(user)
        return render(request, 'portfolio.html', {'portfolios': portfolios})


@login_required
def wallet_view(request):
    user = request.user
    manage_money_form = ManageMoneyForm(request.POST or None)
    if request.method == 'POST':
        if manage_money_form.is_valid():
            transaction = request.POST.get('action')
            amount = manage_money_form.cleaned_data['dollars']
            try:
                perform_money_transaction(user, amount, transaction)
            except ValueError as error:
                messages.warning(request, error)
        return redirect('wallet')

    elif request.method == 'GET':
        wallet = Wallet.objects.get(user=user)
        transactions = Transactions.objects.filter(user=user, symbol="dollar")
        return render(request, 'wallet.html',
                      {'transactions': transactions, 'manage_money_form': manage_money_form, 'wallet': wallet})


@login_required
def crypto_view(request):
    user = request.user
    buy_crypto_form = BuyCryptoForm(request.POST or None)
    sell_crypto_form = SellCryptoForm(request.POST or None)
    user_cryptos = get_user_cryptos(user)
    total_usd = get_total_usd_cryptos(user_cryptos)
    if request.method == 'POST':
        if buy_crypto_form.is_valid():
            usd_amount = Decimal(buy_crypto_form.cleaned_data['usd_amount'])
            crypto = buy_crypto_form.cleaned_data['buy_crypto']
            crypto_price = Decimal(get_coin_price(crypto))
            crypto_amount = usd_amount / crypto_price
            perform_money_transaction(user, usd_amount, 'withdraw')
            perform_crypto_transaction(user, crypto, crypto_amount, 'buy')
        if sell_crypto_form.is_valid():
            crypto_amount = Decimal(sell_crypto_form.cleaned_data['crypto_amount'])
            crypto = sell_crypto_form.cleaned_data['sell_crypto']
            crypto_price = Decimal(get_coin_price(crypto))
            usd_amount = crypto_amount * crypto_price
            perform_crypto_transaction(user, crypto, crypto_amount, 'sell')
            perform_money_transaction(user, usd_amount, 'deposit')
        return redirect('crypto')

    elif request.method == 'GET':
        wallet = Wallet.objects.get(user=user)
        balance = wallet.dollars
        transactions = Transactions.objects.filter(user=user).exclude(symbol="dollar")
        return render(request, 'crypto.html',
                      {'buy_crypto_form': buy_crypto_form, 'sell_crypto_form': sell_crypto_form,
                       'user_cryptos': user_cryptos, 'total_usd': total_usd, 'transactions': transactions,
                       'balance': balance})


def get_price_view(request):
    return get_coin_info(request)
