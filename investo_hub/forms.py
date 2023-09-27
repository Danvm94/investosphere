from decimal import Decimal
from django import forms
from user_management.crypto import get_all_cryptos_names
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date, timedelta
from django.contrib import messages
from user_management.models import Crypto


class TransactionsViewForm(forms.Form):
    tomorrow = date.today() + timedelta(days=1)
    TRANSACTIONS_TYPE_CHOICES = (
        ('all', 'All Transactions'),
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
    )

    transaction_type = forms.ChoiceField(
        choices=TRANSACTIONS_TYPE_CHOICES,
        label='Type',
        initial='all',
        widget=forms.Select(attrs={'class': 'form-control w-auto d-inline-flex'}),
        required=False
    )
    start_date = forms.DateField(
        label='Start',
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control w-auto d-inline-flex', 'max': tomorrow}),
        initial=date.today() - timedelta(days=30),
    )
    end_date = forms.DateField(
        label='End',
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control w-auto d-inline-flex', 'max': tomorrow}),
        initial=tomorrow,
    )


class CryptoTransactionsViewForm(TransactionsViewForm):
    TRANSACTIONS_TYPE_CHOICES = (
        ('all', 'All Transactions'),
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )
    transaction_type = forms.ChoiceField(
        choices=TRANSACTIONS_TYPE_CHOICES,
        label='Type',
        initial='all',
        widget=forms.Select(attrs={'class': 'form-control w-auto d-inline-flex'}),
        required=False
    )
    CRYPTOS_CHOICES = []
    crypto_choice = forms.ChoiceField(
        choices=CRYPTOS_CHOICES,
        label='Crypto',
        initial='all',
        widget=forms.Select(attrs={'class': 'form-control w-auto d-inline-flex'}),
        required=False
    )


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
    def __init__(self, *args, **kwargs):
        self.max_value = kwargs.pop('max_value')
        super().__init__(*args, **kwargs)
        self.fields['withdraw_dollars'] = forms.DecimalField(
            label='',
            widget=forms.NumberInput(attrs={'class': 'd-none', 'id': 'withdraw_dollars_form_decimal'}),
            validators=[
                MinValueValidator(1.00, message='Value must be at least $1.00'),
                MaxValueValidator(50000.00, message='Value cannot exceed $50,000.00'),
                MaxValueValidator(self.max_value, message=f'Value cannot exceed ${self.max_value}'),
            ],
            required=True,
        )
        print(self.max_value)

    text_dollars = forms.CharField(
        label='USD Amount',
        widget=forms.TextInput(attrs={'class': 'form-control balance-modal', 'placeholder': '1.0', 'value': '$.0',
                                      'id': 'withdraw_dollars_form'}),
        required=False,
    )


class BuyCryptoForm(forms.Form):
    CRYPTOS_CHOICES = []
    crypto_select = forms.ChoiceField(
        choices=CRYPTOS_CHOICES,
        label='Type',
        initial='bitcoin',
        widget=forms.Select(attrs={'class': 'form-control w-auto text-center', 'id': 'id_crypto_select_buy'}),
        required=True
    )
    crypto_price = forms.DecimalField(
        label='',
        widget=forms.NumberInput(attrs={'class': 'd-none', 'id': 'crypto_price'}),
    )
    buy_dollars = forms.CharField(
        label='USD Amount',
        widget=forms.TextInput(attrs={'class': 'form-control balance-modal', 'placeholder': '1.0', 'value': '$.0',
                                      'id': 'buy_dollars'}),
    )
    buy_cryptos = forms.CharField(
        label='Crypto Amount',
        widget=forms.TextInput(attrs={'class': 'form-control balance-modal', 'placeholder': '1.0', 'value': '0.0',
                                      'id': 'buy_cryptos'}),
        disabled=True,
        required=False
    )
    buy_cryptos_decimal = forms.DecimalField(
        label='',
        max_digits=40,
        decimal_places=20,
        widget=forms.NumberInput(attrs={'class': 'd-none', 'id': 'buy_cryptos_decimal'}),
    )

    def __init__(self, *args, **kwargs):
        self.max_value = kwargs.pop('max_value')
        super().__init__(*args, **kwargs)
        self.fields['buy_dollars_decimal'] = forms.DecimalField(
            label='',
            widget=forms.NumberInput(attrs={'class': 'd-none', 'id': 'buy_dollars_decimal'}),
            validators=[
                MinValueValidator(1.00, message='Value must be at least $1.00'),
                MaxValueValidator(self.max_value, message=f'Value cannot exceed ${self.max_value}')
            ]
        )


class SellCryptoForm(forms.Form):
    crypto_select = forms.ChoiceField(
        label='Type',
        initial='bitcoin',
        widget=forms.Select(attrs={'class': 'form-control w-auto text-center', 'id': 'id_crypto_select_sell'}),
        required=True
    )
    crypto_price = forms.DecimalField(
        label='',
        widget=forms.NumberInput(attrs={'class': 'd-none', 'id': 'sell-price'}),
    )
    sell_cryptos = forms.CharField(
        label='Crypto Amount',
        widget=forms.TextInput(attrs={'class': 'form-control balance-modal', 'placeholder': '1.0', 'value': '0.0',
                                      'id': 'sell_cryptos'}),
        required=True
    )

    sell_dollars = forms.CharField(
        label='USD Amount',
        widget=forms.TextInput(attrs={'class': 'form-control balance-modal', 'placeholder': '1.0', 'value': '$.0',
                                      'id': 'sell_dollars'}),
        disabled=True,
        required=False
    )
    sell_dollars_decimal = forms.DecimalField(
        label='',
        widget=forms.NumberInput(attrs={'class': 'd-none', 'id': 'sell_dollars_decimal'}),
    )

    def __init__(self, *args, **kwargs):
        self.cryptocurrencies = kwargs.pop('cryptocurrencies', get_all_cryptos_names())
        super().__init__(*args, **kwargs)
        self.fields['crypto_select'].choices = [(crypto.symbol, crypto.symbol.capitalize()) for crypto in
                                                self.cryptocurrencies]
        self.fields['sell_cryptos_decimal'] = forms.DecimalField(
            label='',
            max_digits=40,
            decimal_places=20,
            widget=forms.NumberInput(attrs={'class': 'd-none', 'id': 'sell_cryptos_decimal'}),
        )

    def clean(self):
        cleaned_data = super().clean()
        sell_amount = Decimal(cleaned_data.get('sell_cryptos'))
        crypto = cleaned_data.get('crypto_select')
        for cryptocurrency in self.cryptocurrencies:
            if cryptocurrency.symbol == crypto:
                print(f'{sell_amount} > {cryptocurrency.amount} = {sell_amount > cryptocurrency.amount}')
                if sell_amount > cryptocurrency.amount:
                    raise forms.ValidationError(
                        f"You are unable to sell this quantity of {crypto} because your current balance is "
                        f"{cryptocurrency.amount}.")
                break


class ChartViewForm(forms.Form):
    if Crypto.objects.exists():
        CRYPTOS_CHOICES = [(crypto, crypto.capitalize()) for crypto in get_all_cryptos_names()]
        CRYPTOS_CHOICES.insert(0, ('all', 'All Cryptos'))
        crypto_choice = forms.ChoiceField(
            choices=CRYPTOS_CHOICES,
            label='Crypto',
            initial='all',
            widget=forms.Select(attrs={'class': 'form-control w-auto d-inline-flex'}),
            required=False
        )


def display_form_errors(request, form):
    field_errors = []
    for field_name, errors in form.errors.items():
        for error in errors:
            field_errors.append(f'{error}')

    for field_error in field_errors:
        messages.warning(request, field_error)
