# Generated by Django 4.1 on 2022-08-19 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avantar',
            new_name='avatar',
        ),
    ]