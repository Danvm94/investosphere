from django import forms
from investosphere.settings import CRYPTOCURRENCIES
from .models import Portfolio, Wallet


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name']  # Include only the 'name' field in the form


class ManageMoneyForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['dollars']


class ManageCryptoForm(forms.Form):
    crypto = forms.ChoiceField(choices=[(crypto, crypto) for crypto in CRYPTOCURRENCIES])
    usd_amount = forms.DecimalField(min_value=1.00)
