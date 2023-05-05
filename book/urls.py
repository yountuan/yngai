from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (BookCreateApiView,
                    BookListSerializer,
                    BookUpdateApiView,
                    BookDestroyApiView,
                    CategoryCreateApiView,
                    CategoryListApiView,
                    CategoryUpdateApiView,
                    CategoryDestroyApiView,
                    )


urlpatterns = [
    path('create/', BookCreateApiView.as_view(), name='prod-create'),
    path('list/', BookListSerializer.as_view(), name='prod-list'),
    path('update/<int:id>/', BookUpdateApiView.as_view(), name='update'),
    path('delete/<int:id>/', BookDestroyApiView.as_view(), name='delete'),
    path('cat_create/', CategoryCreateApiView.as_view(), name='cat_create'),
    path('cat_list/', CategoryListApiView.as_view(), name='cat_list'),
    path('cat_update/<int:id>/', CategoryUpdateApiView.as_view(), name='cat_update'),
    path('cat_delete/<int:id>/', CategoryDestroyApiView.as_view(), name='cat_delete'),

    # path('', include(router.urls)),
]