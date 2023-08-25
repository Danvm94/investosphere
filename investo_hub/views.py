from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wallet, Portfolio, Transactions
from .forms import PortfolioForm, ManageMoneyForm
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
                manageMoney(user, amount, 'deposit')
            elif action == 'withdraw':
                try:
                    manageMoney(user, amount, 'withdraw')
                except ValueError as error:
                    messages.warning(request, error)
        return redirect('wallet')
    elif request.method == 'GET':
        wallet = Wallet.objects.get(user=user)
        balance = wallet.dollars
        transactions = Transactions.objects.filter(user=user, symbol="dollar")
        form = ManageMoneyForm(request.POST)
        return render(request, 'wallet.html', {'balance': balance, 'transactions': transactions, 'form': form})


def manageMoney(user, amount, transaction):
    wallet = get_or_create_wallet(user)
    if transaction == "deposit":
        deposit_into_wallet(user, wallet, amount)
    elif transaction == "withdraw":
        withdraw_from_wallet(user, wallet, amount)
    wallet.save()


def deposit_into_wallet(user, wallet, amount):
    wallet.dollars += amount
    transaction = Transactions.objects.create(
        user=user,  type="deposit", symbol="dollar", amount=amount)


def withdraw_from_wallet(user, wallet, amount):
    if wallet.dollars >= amount:
        wallet.dollars -= amount
        transaction = Transactions.objects.create(
            user=user,  type="withdraw", symbol="dollar", amount=-amount)
    else:
        raise ValueError(
            "Insufficient funds in your wallet. "
            "The withdrawal amount exceeds your available balance.")


def get_or_create_wallet(user):
    try:
        wallet = Wallet.objects.get(user=user)
    except Wallet.DoesNotExist:
        wallet = Wallet.objects.create(user=user)
    return wallet
