from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Crypto
import requests
import os


def validate_crypto(value):
    coin_api = os.environ.get('COIN_API_URL')
    response = requests.get(coin_api + f'/coins/{value}')
    if response.status_code != 200:
        raise ValidationError("The crypto {} does not exist.".format(value))
    if Crypto.objects.filter(name=value).exists():
        raise ValidationError("The crypto {} is already added to the system.".format(value))


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddCryptoForm(forms.Form):
    crypto = forms.CharField(
        label='Crypto',
        widget=forms.TextInput(attrs={'class': ''}),
        validators=[validate_crypto])
