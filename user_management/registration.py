from investo_hub.transactions import get_or_create_wallet
from django.contrib import messages
from django.contrib.auth import login


def register_user(request, user):
    login(request, user)
    get_or_create_wallet(user)
    messages.success(request, 'Registration successful!')
