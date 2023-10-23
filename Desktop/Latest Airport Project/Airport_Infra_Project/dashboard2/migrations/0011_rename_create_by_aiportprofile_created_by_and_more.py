# Generated by Django 4.1.3 on 2023-05-11 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_aiportprofile_create_by_aiportprofile_date_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aiportprofile',
            old_name='create_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='aiportproject',
            old_name='create_by',
            new_name='created_by',
        ),
        migrations.AddField(
            model_name='aiportprofile',
            name='edited_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aiportproject',
            name='edited_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]