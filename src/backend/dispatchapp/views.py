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

    def post(self, request):
        data = request.data

        # extracting the data from the request
        name = data['name']
        email = data['email']
        message = data['message']

        try:
            # creating the instance object
            notif = Notification.objects.create(
                name=name,
                email=email,
                message=message,
            )
            # serializing the data for validation
            serializer = NotificationSerializer(notif, many=False)
        except:
            errorMessage = {"detail": "Something went wrong!!"}
            return Response(errorMessage, status=status.HTTP_400_BAD_REQUEST)

        # send the email using the send_mail django function
        send_mail(
            'subject',
            message,
            None,
            [email],
            fail_silently=False
        )

        return Response(serializer.data)
