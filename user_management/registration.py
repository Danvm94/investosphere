from investo_hub.transactions import get_or_create_wallet
from investo_hub.portfolios import get_or_create_portfolio
from django.contrib import messages
from django.contrib.auth import login


def register_user(request, user):
    login(request, user)
    get_or_create_wallet(user)
    get_or_create_portfolio(user, user.username)
    messages.success(request, 'Registration successful!')


