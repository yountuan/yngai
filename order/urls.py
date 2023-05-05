from django.urls import path, include
from .views import OrderItemView, OrderListView, CheckTokenAPIView, PayApiView, TokenAPIView

urlpatterns = [
    path('order_item/', OrderItemView.as_view()),
    path('order_item/cart/', OrderListView.as_view()),
    path('order_item/check/', CheckTokenAPIView.as_view()),
    path('get_token/', TokenAPIView.as_view()),
    path('pay/', PayApiView.as_view()),
]