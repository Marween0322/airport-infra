# Generated by Django 3.2.8 on 2022-08-31 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0032_alter_experience_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='grad_year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]