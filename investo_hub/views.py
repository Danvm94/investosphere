from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wallet, Portfolio
import requests
import os

def portfolio_view(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    balance = wallet.dollars
    portfolios = Portfolio.objects.filter(user=user)
    return render(request, 'portfolio.html', {'balance': balance, 'portfolios': portfolios})