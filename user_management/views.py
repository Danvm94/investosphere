from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .registration import register_user


from investo_hub.cryptos import request_coin_cache
from .newsapi import get_news_api


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            register_user(request, user)
            # Redirect to the home page or another appropriate URL
            return redirect('home')
        else:
            # If form is not valid, collect field-specific error messages
            field_errors = []
            for field_name, errors in form.errors.items():
                for error in errors:
                    field_errors.append(f'{form.fields[field_name].label}: {error}')
            if field_errors:
                for field_error in field_errors:
                    messages.warning(request, field_error)
            return redirect('register')

    elif request.method == 'GET':
        form = RegistrationForm()
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
    messages.success(request, "You are now logged out")
    return redirect('home')


def home_view(request):
    articles = get_news_api()
    cryptos_trending = request_coin_cache()
    return render(request, 'home.html', {'articles': articles, 'cryptos_trending': cryptos_trending})
