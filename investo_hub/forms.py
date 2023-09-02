from django import forms
from investosphere.settings import CRYPTOCURRENCIES
from .models import Portfolio, Wallet
from django.core.validators import MinValueValidator, MaxValueValidator


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name']  # Include only the 'name' field in the form


class DepositMoneyForm(forms.Form):
    text_dollars = forms.CharField(
        label='USD Amount',
        widget=forms.TextInput(attrs={'class': 'form-control balance-modal', 'placeholder': '1.0', 'value': '$.0',
                                      'id': 'deposit_dollars_form'}),
    )
    deposit_dollars = forms.DecimalField(
        label='',
        widget=forms.NumberInput(attrs={'class': 'd-none', 'id': 'deposit_dollars_form_decimal'}),
        validators=[
            MinValueValidator(1.00, message='Value must be at least $1.00'),
            MaxValueValidator(50000.00, message='Value cannot exceed $50,000.00')
        ]
    )


class WithdrawMoneyForm(forms.Form):
    text_dollars = forms.CharField(
        label='USD Amount',
        widget=forms.TextInput(attrs={'class': 'form-control balance-modal', 'placeholder': '1.0', 'value': '$.0',
                                      'id': 'withdraw_dollars_form'}),
    )
    withdraw_dollars = forms.DecimalField(
        label='',
        widget=forms.NumberInput(attrs={'class': 'd-none', 'id': 'withdraw_dollars_form_decimal'}),
    )

    def __init__(self, *args, **kwargs):
        max_value = kwargs.pop('max_value', 50000.00)  # Default to $50,000.00 if max_value is not provided
        super().__init__(*args, **kwargs)
        self.fields['withdraw_dollars'].validators.extend([
            MinValueValidator(1.00, message='Value must be at least $1.00'),
            MaxValueValidator(max_value, message=f'Value cannot exceed ${max_value:.2f}')
        ])


class BuyCryptoForm(forms.Form):
    buy_crypto = forms.ChoiceField(choices=[(crypto, crypto) for crypto in CRYPTOCURRENCIES])
    usd_amount = forms.DecimalField(min_value=1.00)


class SellCryptoForm(forms.Form):
    sell_crypto = forms.ChoiceField(choices=[(crypto, crypto) for crypto in CRYPTOCURRENCIES])
    crypto_amount = forms.DecimalField(min_value=0.00000000000001)


class CreatePortfolioForm(forms.Form):
    class Meta:
        model = Portfolio
        fields = ['name']  # Include only the 'name' field in the form
