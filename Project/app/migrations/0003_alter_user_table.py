# Generated by Django 4.1.12 on 2023-10-26 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_options_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]
