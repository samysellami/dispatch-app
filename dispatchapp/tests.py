from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse

from django.contrib.auth import get_user_model
from dispatchapp.models import Notification
User = get_user_model()


class DispatchAPIViewTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='samy', email='samy.sellami@hotmail.com')
        user.set_password('password')
        user.save()

        notif = Notification.objects.create(
            name='Sellami Sami',
            subject='notification',
            email='samy.sellami@hotmail.com',
            phoneNumber='+79600603696',
            message='This is a notification'
        )

    def test_created_user_notif(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)
        qs = User.objects.filter(username='samy')
        self.assertEqual(qs.count(), 1)

        qs = Notification.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_notif_success(self):
        url = api_reverse('api-dispatch:notif-create')
        data = {
            'name': 'Sellami Sami',
            'subject': 'notification',
            'email': 'samy.sellami@hotmail.com',
            # 'phoneNumber': '+79600603696',
            'message': 'This is a notification'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['detail'], 'Thank you for your notification, please check you email!!')

    def test_notif_unvalid_email_fail(self):
        url = api_reverse('api-dispatch:notif-create')
        data = {
            'email': 'samy.sellamihotmail.com',
            'phoneNumber': '+79600603696',
            'message': 'This is a notification'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Invalid data, please correct your input and try again!!')

    def test_notif_unvalid_phone_fail(self):
        url = api_reverse('api-dispatch:notif-create')
        data = {
            'email': 'samy.sellami@hotmail.com',
            'phoneNumber': '+99060367',
            'message': 'This is a notification'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Invalid data, please correct your input and try again!!')

    def test_notif_unverified_phone_fail(self):
        url = api_reverse('api-dispatch:notif-create')
        data = {
            'email': 'samy.sellami@hotmail.com',
            'phoneNumber': '+79600603697',
            'message': 'This is a notification'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['detail'],
            'Sorry, free Twilio accounts do not allow sending SMS to non verified phone numbers!'
        )
