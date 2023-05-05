# from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import permissions, status
from .permissions import AnonPermissionOnly
from authentication.serializers import RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from base.models import Vendor


User = get_user_model()


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterApiView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def post(self, request):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            user = User.objects.create(
                username=request.data['username'],
                email=request.data['email'],
            )
            user.set_password(request.data['password'])
            user.save()
            vendor = Vendor.objects.create(
                user=user,
                company_name=request.data['company_name'],
                phone_number=request.data['phone_number'],
            )
            vendor.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)