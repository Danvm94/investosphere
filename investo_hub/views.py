from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wallet, Portfolio
from .forms import PortfolioForm
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
    wallet = Wallet.objects.get(user=user)
    balance = wallet.dollars
    return render(request, 'wallet.html', {'balance': balance})
