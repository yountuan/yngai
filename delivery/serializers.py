from rest_framework import serializers
from base.models import *

class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['data']