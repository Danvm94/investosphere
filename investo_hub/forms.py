from django import forms
from investosphere.settings import CRYPTOCURRENCIES
from .models import Portfolio, Wallet
from .portfolios import get_all_portfolios


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name']  # Include only the 'name' field in the form


class ManageMoneyForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['dollars']


class BuyCryptoForm(forms.Form):
    # def __init__(self, *args, user=None, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     portfolios = get_all_portfolios(user)
    #     portfolio_choices = [(portfolio.id, portfolio.name) for portfolio in portfolios]
    #     self.fields['portfolio_choice'] = forms.ChoiceField(choices=portfolio_choices)

    buy_crypto = forms.ChoiceField(choices=[(crypto, crypto) for crypto in CRYPTOCURRENCIES])
    usd_amount = forms.DecimalField(min_value=1.00)


class SellCryptoForm(forms.Form):
    sell_crypto = forms.ChoiceField(choices=[(crypto, crypto) for crypto in CRYPTOCURRENCIES])
    crypto_amount = forms.DecimalField(min_value=0.00000000000001)


class CreatePortfolioForm(forms.Form):
    class Meta:
        model = Portfolio
        fields = ['name']  # Include only the 'name' field in the form
