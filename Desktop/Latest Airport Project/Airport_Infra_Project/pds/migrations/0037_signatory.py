# Generated by Django 3.2.8 on 2022-09-19 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0036_auto_20220915_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signatory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_designate_rate', models.CharField(blank=True, max_length=200, null=True)),
                ('pay_designate_rate_possition', models.CharField(blank=True, max_length=200, null=True)),
                ('pay_prepare', models.CharField(blank=True, max_length=200, null=True)),
                ('pay_prepare_possition', models.CharField(blank=True, max_length=200, null=True)),
                ('pay_approve', models.CharField(blank=True, max_length=200, null=True)),
                ('pay_approve_possition', models.CharField(blank=True, max_length=200, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]