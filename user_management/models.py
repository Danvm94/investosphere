from django.db import models


class Crypto(models.Model):
    name = models.CharField(max_length=100, unique=True)
