# Generated by Django 3.2.8 on 2022-06-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0010_leave_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='updated_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
