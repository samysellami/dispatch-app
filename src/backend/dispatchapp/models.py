from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator


class Notification(models.Model):
    phoneNumber_valid = RegexValidator(
        regex=r"^\+?7?\d{8,15}$", message='invalid phone number, please use the format +7xxxxxxxxxx')
    email_valid = EmailValidator(message='invalid email, please use the format name@example.com')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, validators=[email_valid], null=True, blank=True)
    phoneNumber = models.CharField(validators=[phoneNumber_valid], max_length=16, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=254, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)
