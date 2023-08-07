from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stocks(models.Model):
    # Owner's ID, it is a foreignkey from Django's built in user system
    owner_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owned_stocks"
    )
    ammount = models.FloatField()
    stock_id = models.IntegerField()

class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )
    
    TRANSACTION_CHOICES = [
    ("BUY", "Buy"),
    ("SELL", "Sell"),
    ]
    transaction_type = models.CharField(
        max_length=10, choices=TRANSACTION_CHOICES, unique=True)
    stock_id = models.IntegerField()
    transaction_ammount = models.FloatField()
    transaction_date = models.DateTimeField(auto_now=True)
    