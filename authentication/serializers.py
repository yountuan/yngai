from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from base.models import Vendor
from django.contrib.auth import get_user_model


User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        write_only=True,
        required=True
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn`t match."}
            )
        return attrs


class VendorSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(many=False)

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = User.objects.create(**user_data)

        vendor = Vendor.objects.create(user=user, **validated_data)
        return vendor

    class Meta:
        model = Vendor
        fields = ['user', 'company_name', 'phone_number']



