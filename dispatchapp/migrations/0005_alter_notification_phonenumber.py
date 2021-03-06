# Generated by Django 3.2.8 on 2021-10-22 10:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatchapp', '0004_notification_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?7?\\d{8,15}$')]),
        ),
    ]
