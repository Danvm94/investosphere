from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
# Create your views here.


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to the home page or another appropriate URL
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
