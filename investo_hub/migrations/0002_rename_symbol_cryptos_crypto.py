# Generated by Django 4.2.4 on 2023-09-26 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investo_hub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptos',
            old_name='symbol',
            new_name='crypto',
        ),
    ]
