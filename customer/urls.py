from django.urls import path

from .views import (
    RegisterApiView,
    MyObtainPairView
)

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair')
]