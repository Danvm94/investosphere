from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wallet, Portfolio, Transactions
from .forms import PortfolioForm, ManageMoneyForm
from .transactions import perform_money_transaction
from .cryptos import get_top_gainers
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
    form = ManageMoneyForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            transaction = request.POST.get('action')
            amount = form.cleaned_data['dollars']
            try:
                perform_money_transaction(user, amount, transaction)
            except ValueError as error:
                messages.warning(request, error)
        return redirect('wallet')
    elif request.method == 'GET':
        wallet = Wallet.objects.get(user=user)
        balance = wallet.dollars
        transactions = Transactions.objects.filter(user=user, symbol="dollar")
        return render(request, 'wallet.html', {'balance': balance, 'transactions': transactions, 'form': form})


@login_required
def crypto_view(request):
    cryptos_trending = get_top_gainers(5)
    return render(request, 'crypto.html', {'cryptos_trending': cryptos_trending})
