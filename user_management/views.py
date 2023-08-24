from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from investo_hub.models import Wallet
import requests
import os
# Create your views here.


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            wallet = Wallet.objects.create(user=user, dollars=1000)
            messages.success(request, 'Registration successful!')
            # Redirect to the home page or another appropriate URL
            return redirect('home')
    else:
        form = RegistrationForm()

    # If form is not valid, collect field-specific error messages
    field_errors = []
    for field_name, errors in form.errors.items():
        for error in errors:
            field_errors.append(f'{form.fields[field_name].label}: {error}')
    if field_errors:
        for field_error in field_errors:
            messages.warning(request, field_error)

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the dashboard or desired page
            messages.success(request, "You are now logged in")
            return redirect('home')
        else:
            # Invalid login, show an error message
            messages.warning(request, "Invalid username or password.")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    # Redirect to the home page
    return redirect('home')


def home_view(request):
    NEWSAPI_KEY = os.environ.get('NEWSAPI_KEY')
    NEWSAPI_URL = os.environ.get('NEWSAPI_URL')
    params = {
        'apiKey': NEWSAPI_KEY,
        'language': 'en',
        'q': 'crypto OR stock',
        'sortBy': 'relevancy'
    }
    response = requests.get(NEWSAPI_URL, params=params)
    news_data = response.json()
    articles = news_data['articles'][:4]

    return render(request, 'home.html', {'articles': articles})
