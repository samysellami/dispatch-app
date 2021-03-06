# Generated by Django 3.2.8 on 2021-10-23 13:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatchapp', '0009_alter_notification_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator(message='invalid email, please use the format xxx@xxx.xx')]),
        ),
    ]
