from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wallet, Portfolio, Transactions
from .forms import PortfolioForm, ManageMoneyForm, ManageCryptoForm
from .transactions import perform_money_transaction
from .cryptos import get_top_gainers, get_all_coins, get_price
import os


@login_required
def portfolio_view(request):
    user = request.user
    form = PortfolioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            Portfolio.objects.create(user=user, name=name)
            return redirect('portfolio')
    elif request.method == 'GET':
        portfolios = Portfolio.objects.filter(user=user)
        return render(request, 'portfolio.html', {'portfolios': portfolios, 'form': form})


@login_required
def wallet_view(request):
    user = request.user
    manage_money_form = ManageMoneyForm(request.POST or None)
    manage_crypto_form = ManageCryptoForm(request.POST or None)
    if request.method == 'POST':
        if manage_money_form.is_valid():
            transaction = request.POST.get('action')
            amount = manage_money_form.cleaned_data['dollars']
            try:
                perform_money_transaction(user, amount, transaction)
            except ValueError as error:
                messages.warning(request, error)
        if manage_crypto_form.is_valid():
            transaction = request.POST.get('action')
            print(transaction)
        return redirect('wallet')
    elif request.method == 'GET':
        wallet = Wallet.objects.get(user=user)
        balance = wallet.dollars
        transactions = Transactions.objects.filter(user=user, symbol="dollar")
        cryptos_list = get_all_coins
        return render(request, 'wallet.html',
                      {'balance': balance, 'transactions': transactions, 'manage_money_form': manage_money_form,
                       'manage_crypto_form': manage_crypto_form,
                       'cryptos_list': cryptos_list})


@login_required
def crypto_view(request):
    cryptos_trending = get_top_gainers(10)
    return render(request, 'crypto.html', {'cryptos_trending': cryptos_trending})


def get_price_view(request):
    return get_price(request)
