from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail

from .notification import notification
from .models import Notification
from .serializers import NotificationSerializer


class DispatchAPIView(APIView):
    permission_classes = []

    # def get(self, request):
    #     return Response(notification)

    def post(self, request):
        data = request.data

        name = data['name'],
        email = data['email'],
        message = data['message'],

        notif = Notification.objects.create(
            name=name,
            email=email,
            message=message,
        )
        serializer = NotificationSerializer(notif, many=False)
        # send_mail(
        #     'subject',
        #     'This is a notification',
        #     'amethyst_test@hotmail.com',
        #     ['samy.sellami@hotmail.com'],
        #     fail_silently=False
        # )

        return Response(serializer.data)
