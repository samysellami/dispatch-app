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
        # print('data= ', data)
        name = data.get('name', None)
        subject = data.get('subject', None)
        email = data.get('email', None)
        message = data.get('message', None)
        phoneNumber = data.get('phoneNumber', None)

        try:
            # serializing the data for validation
            serializer = NotificationSerializer(data=data, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        except:
            return Response(
                {"detail": 'Invalid data, please correct your input and try again!!'},
                status=status.HTTP_400_BAD_REQUEST)

        # sending the email using the send_mail django function
        if (email is not None) and (len(email) != 0):
            send_mail(
                subject,
                message,
                None,
                [email],
                fail_silently=False
            )

        # Sending SMS using TWILIO
        if (phoneNumber is not None) and (len(phoneNumber) != 0):
            try:
                account_sid = TWILIO_ACCOUNT_SID
                auth_token = TWILIO_AUTH_TOKEN
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body=message,
                    from_='+13868544713',
                    to=phoneNumber
                )
            except:
                return Response(
                    {"detail": 'Sorry, free Twilio account does not allow sending SMS to non verified phone numbers!'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        data_ = serializer.data
        data_['detail'] = "Thank you for your notification, plase check you email!!"
        return Response(data_, status=status.HTTP_201_CREATED)
