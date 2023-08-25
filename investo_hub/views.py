from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wallet, Portfolio, Transactions
from .forms import PortfolioForm, ManageMoneyForm
from .transactions import perform_money_transaction, deposit_into_wallet, withdraw_from_wallet, get_or_create_wallet
import requests
import os


def portfolio_view(request):
    user = request.user

    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_portfolio = Portfolio.objects.create(user=user, name=name)
            return redirect('portfolio')
    else:
        form = PortfolioForm()

    wallet = Wallet.objects.get(user=user)
    balance = wallet.dollars
    portfolios = Portfolio.objects.filter(user=user)

    return render(request, 'portfolio.html', {'balance': balance, 'portfolios': portfolios, 'form': form})


def wallet_view(request):
    user = request.user
    if request.method == 'POST':
        form = ManageMoneyForm(request.POST)
        if form.is_valid():
            action = request.POST.get('action')
            amount = form.cleaned_data['dollars']
            if action == 'deposit':
                perform_money_transaction(user, amount, 'deposit')
            elif action == 'withdraw':
                try:
                    perform_money_transaction(user, amount, 'withdraw')
                except ValueError as error:
                    messages.warning(request, error)
        return redirect('wallet')
    elif request.method == 'GET':
        wallet = Wallet.objects.get(user=user)
        balance = wallet.dollars
        transactions = Transactions.objects.filter(user=user, symbol="dollar")
        form = ManageMoneyForm(request.POST)
        return render(request, 'wallet.html', {'balance': balance, 'transactions': transactions, 'form': form})
