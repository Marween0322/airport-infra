# Generated by Django 4.1.3 on 2023-05-11 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_aiportprofile_airport_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiportprofile',
            name='apron_num',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
