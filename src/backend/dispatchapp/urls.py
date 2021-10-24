from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DispatchAPIView.as_view(), name='notif-create'),
]

app_name = 'dipatchapp'
