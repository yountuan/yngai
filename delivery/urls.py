from django.urls import path, include
from .views import DeliveryApiView

urlpatterns = [
    path('delivery/', DeliveryApiView.as_view(), name='delivery'),
]
