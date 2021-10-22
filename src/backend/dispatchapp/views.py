from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from twilio.rest import Client

from .notification import notification
from .models import Notification
from .serializers import NotificationSerializer
from backend.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN


class DispatchAPIView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):

        # Sending email using SMTP

        # extracting the data from the request
        data = request.data
        name = data['name']
        subject = data['subject']
        email = data['email']
        message = data['message']
        phone = data['phone']

        try:
            # creating the instance object
            notif = Notification.objects.create(
                name=name,
                subject=subject,
                email=email,
                message=message,
                phoneNumber=phone,
            )
            # serializing the data for validation
            serializer = NotificationSerializer(data=data, many=False)
            serializer.is_valid(raise_exception=True)
        except ValidationError as error:
            return Response({"detail": error}, status=status.HTTP_400_BAD_REQUEST)

        # sending the email using the send_mail django function
        send_mail(
            subject,
            message,
            None,
            [email],
            fail_silently=False
        )

        # Sending sms using TWILIO
        try:
            account_sid = TWILIO_ACCOUNT_SID
            auth_token = TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=message,
                from_='+13868544713',
                to=phone
            )
        except:
            return Response(
                {"detail": 'Cannot send a message to this phone number!!'},
                status=status.HTTP_400_BAD_REQUEST
            )

        data_ = serializer.data
        data_['detail'] = "Thank you for your notification, plase verify you email!!"
        return Response(data_, status=status.HTTP_201_CREATED)
