from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dollars = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Cryptos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=40, decimal_places=20, default=Decimal('0.0'))


class Stocks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    shares = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
