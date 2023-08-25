from django import forms
from .models import Portfolio, Wallet


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name']  # Include only the 'name' field in the form


class ManageMoneyForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['dollars']
