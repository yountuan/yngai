from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import Delivery
from .serializers import DeliverySerializer

class DeliveryApiView(APIView):
    # permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializers = DeliverySerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)