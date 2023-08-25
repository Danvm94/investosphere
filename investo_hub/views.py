from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wallet, Portfolio, Transactions
from .forms import PortfolioForm, AddMoneyForm
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
        form = AddMoneyForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['dollars']
            addMoney(user=user, amount=amount)
            return redirect('wallet')
    elif request.method == 'GET':
        wallet = Wallet.objects.get(user=user)
        balance = wallet.dollars
        transactions = Transactions.objects.filter(user=user, type="money")
        form = AddMoneyForm(request.POST)
        return render(request, 'wallet.html', {'balance': balance, 'transactions': transactions, 'form': form})


def addMoney(user, amount):
    try:
        wallet = Wallet.objects.get(user=user)
        wallet.dollars += amount
        wallet.save()
        transaction_success = True
    except Wallet.DoesNotExist:
        wallet = Wallet.objects.create(user=user, dollars=amount)
        transaction_success = False

    transaction = Transactions.objects.create(
        user=user,  type="money", symbol="dollar", amount=amount)

    return transaction_success
