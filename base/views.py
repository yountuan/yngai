from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class TestAPIView(APIView):
    def post(self, request):
        return Response(request.data)
