from django import forms
from .models import Portfolio, Wallet


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name']  # Include only the 'name' field in the form


class AddMoneyForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['dollars']
    def clean_dollars(self):
        dollars = self.cleaned_data.get('dollars')
        if dollars is not None and (dollars < 1.00 or dollars > 99999.99):
            raise forms.ValidationError("Value must be between 1.00 and 99999.99.")
        return dollars
