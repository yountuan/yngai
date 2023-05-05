from django.urls import path

from base.views import TestAPIView
from .views import (BookListAPIView,
                    BookFilialListAPIView,
                    BookedBookFilialAPIView,
                    FilialCreateApiView,
                    FilialListApiView,
                    FilialUpdateApiView,
                    FilialDestroyApiView,
                    CategoryListAPIView,
                    GetPagesNumber,
                    BookFilialCreateAPIView
                    )

urlpatterns = [
    path('', BookListAPIView.as_view(), name='books'),
    path('pages/', GetPagesNumber.as_view(), name='books_pages'),
    path('filials/', BookFilialListAPIView.as_view(), name='book_filials'),
    path('book_filial/add/', BookFilialCreateAPIView.as_view(), name='book_filials_create'),
    path('my_filials/', BookedBookFilialAPIView.as_view(), name='book_in_my_filials'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),


    path('test/', TestAPIView.as_view()),

    path('create/', FilialCreateApiView.as_view(), name='create'),
    path('list/', FilialListApiView.as_view(), name='list'),
    path('update/<int:id>/', FilialUpdateApiView.as_view(), name='update'),
    path('delete/<int:id>/', FilialDestroyApiView.as_view(), name='delete'),
]