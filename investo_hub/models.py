from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dollars = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_amount(self):
        formatted_value = '{:,.2f}'.format(self.dollars)
        return formatted_value


class Cryptos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=40, decimal_places=20, default=Decimal('0.0'))

    def formatted_amount(self):
        formatted = format(self.amount, f".20f")
        return formatted.rstrip('0').rstrip('.') if '.' in formatted else formatted


class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=40, decimal_places=20, default=Decimal('0.0'))
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_amount(self):
        if self.symbol == 'dollar':
            if self.amount > 0:
                formatted_value = '+ ${:,.2f}'.format(self.amount)
            else:

                formatted_value = '- ${:,.2f}'.format(self.amount * -1)
            return formatted_value
        else:
            formatted = format(self.amount, f".20f")
            return formatted.rstrip('0').rstrip('.') if '.' in formatted else formatted
