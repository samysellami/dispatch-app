# Generated by Django 3.2.8 on 2021-10-23 15:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatchapp', '0011_auto_20211023_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator(message='invalid email, please use the format name@example.com')]),
        ),
        migrations.AlterField(
            model_name='notification',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='invalid phone number, please use the format +7xxxxxxxxxx', regex='^\\+?7?\\d{8,15}$')]),
        ),
    ]
