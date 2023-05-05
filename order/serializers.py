from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from base.models import *
from books.serializers import BookFilialSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source="token.token", read_only=True)

    class Meta:
        model = OrderItem
        fields = ['book_filial', 'quantity', 'token']

    def validate(self, attrs):
        token: CartToken
        user = self.context['request'].user
        token = CartToken.objects.filter(client__user_id=user.pk).last()
        if token:
            if token.creation_date + timedelta(days=1) < timezone.now():
                token.delete()
        return attrs

    def save(self):
        validated_data = self.validated_data
        user = self.context['request'].user
        token = CartToken.objects.filter(client__user_id=user.pk).last()
        book_filial = validated_data['book_filial']

        if not token:
            token = CartToken.objects.create(
                client=Client.objects.get(user_id=user.pk)
             )

        order_item: OrderItem
        order_item, created = OrderItem.objects.get_or_create(
            token=token,
            price=book_filial.price,
            book_filial=book_filial
        )

        order_item.quantity += validated_data['quantity']
        order_item.save()

        return order_item


class OrderItemListSerializer(serializers.ModelSerializer):
    book_filial = BookFilialSerializer(many=False)
    token = serializers.CharField(source='token.token')

    class Meta:
        model = OrderItem
        fields = ['book_filial', 'token', 'quantity', 'price']


class PaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['data']


