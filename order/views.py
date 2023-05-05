from django.db.models import Sum, F
from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import OrderItem, CartToken
from .serializers import OrderItemSerializer, OrderItemListSerializer, PaySerializer


class OrderItemView(CreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class OrderListView(ListAPIView):
    serializer_class = OrderItemListSerializer

    def get_queryset(self):
        return OrderItem.objects.filter(
            token__client__user_id=self.request.user.pk
        )


class CheckTokenAPIView(ListAPIView):
    serializer_class = OrderItemListSerializer

    def get_queryset(self):
        token = self.request.GET["token"]
        if CartToken.validate_token(token):
            return OrderItem.objects.filter(
                token__token=token
            )
        else:
            raise ValidationError("No such token")

    def post(self, request):
        token = self.request.GET["token"]
        if CartToken.validate_token(token):
            token = CartToken.objects.get(token=token)
            order_items = OrderItem.objects.filter(
                token=token.pk
            )

            for oi in order_items:
                oi: OrderItem
                oi.book_filial.quantity -= oi.quantity
                oi.book_filial.save()

            token.delete()
            return Response(self.request.GET["token"], status=status.HTTP_200_OK)
        return Response("No such token", status=status.HTTP_404_NOT_FOUND)


class PayApiView(APIView):
    # permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializers = PaySerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenAPIView(APIView):
    def get(self, request):
        token = CartToken.objects.get(
            client__user_id=request.user.pk
        )
        s = OrderItem.objects.filter(
                    token_id=token.pk
                ).aggregate(sum=Sum(F('price')*F('quantity')))['sum']
        return Response(
            {
                "token": token.token,
                "sum": s,
                "discount":  s * 0.05
            },
            status=status.HTTP_200_OK
        )
