# Generated by Django 4.0.4 on 2023-10-04 10:25

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_aiportprofile_airport_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiportproject',
            name='contract_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=100),
        ),
        migrations.AlterField(
            model_name='aiportproject',
            name='fund_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=100),
        ),
    ]
