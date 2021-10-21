from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

from .notification import notification
from .models import Notification
from .serializers import NotificationSerializer


class DispatchAPIView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):

        # extracting the data from the request
        data = request.data
        name = data['name']
        subject = data['subject']
        email = data['email']
        message = data['message']

        try:
            # creating the instance object
            notif = Notification.objects.create(
                name=name,
                subject=subject,
                email=email,
                message=message,
            )
            # serializing the data for validation
            serializer = NotificationSerializer(data=data, many=False)
            serializer.is_valid(raise_exception=True)
        except ValidationError as error:
            return Response({"detail": error}, status=status.HTTP_400_BAD_REQUEST)

        # send the email using the send_mail django function
        send_mail(
            subject,
            message,
            None,
            [email],
            fail_silently=False
        )

        data_ = serializer.data
        data_['detail'] = "Thank you for your notification, plase verify you email!!"
        return Response(data_, status=status.HTTP_201_CREATED)
