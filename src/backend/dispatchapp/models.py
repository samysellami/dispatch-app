from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phoneNumber = PhoneNumberField(unique=True, null=True, blank=True)  # Here
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=254, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)
