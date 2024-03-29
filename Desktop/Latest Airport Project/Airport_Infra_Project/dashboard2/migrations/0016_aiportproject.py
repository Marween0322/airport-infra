# Generated by Django 4.1.3 on 2023-05-30 06:25

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_delete_aiportproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='AiportProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('fund_org', models.CharField(blank=True, max_length=255, null=True)),
                ('fund_amount', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=14)),
                ('fund_year', models.CharField(blank=True, max_length=255, null=True)),
                ('contract_mi', models.CharField(blank=True, max_length=255, null=True)),
                ('contract_contractor', models.CharField(blank=True, max_length=199, null=True)),
                ('contract_amount', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=14)),
                ('contract_rev', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=14)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('original', models.DateTimeField(blank=True, null=True, verbose_name='original')),
                ('revised', models.DateTimeField(blank=True, null=True, verbose_name='revised')),
                ('status_desc', models.CharField(blank=True, max_length=1000, null=True)),
                ('slippage', models.CharField(blank=True, max_length=200, null=True)),
                ('agency', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=1000, null=True)),
                ('area', models.CharField(blank=True, max_length=200, null=True)),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('certificate', models.CharField(blank=True, max_length=200, null=True)),
                ('recouped_pay', models.CharField(blank=True, max_length=200, null=True)),
                ('progress', models.IntegerField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('edited_by', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True, verbose_name='create_date')),
                ('date_edited', models.DateTimeField(blank=True, null=True, verbose_name='edit_date')),
            ],
        ),
    ]
