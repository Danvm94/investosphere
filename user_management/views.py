from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
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
            return redirect('home')
        else:
            # Invalid login, show an error message
            messages.warning(request, "Invalid username or password.")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    # Redirect to the home page or any other desired page
    return redirect('home')


def home_view(request):
    return render(request, 'home.html')
