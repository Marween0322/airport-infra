# Generated by Django 4.1.3 on 2023-04-12 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_aknowledge_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='aknowledge',
            name='create_by_id',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]