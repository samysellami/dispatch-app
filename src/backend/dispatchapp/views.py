from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .notification import notification
# Create your views here.


def test(request):
    return JsonResponse('Hello', safe=False)


class DispatchAPIView(APIView):

    def get(self, request):
        return Response(notification)
