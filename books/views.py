from datetime import timedelta

from django.http import Http404
from django.utils import timezone

from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import Book, Category, BookFilial, OrderItem, Vendor, Filial
from book.serializers import CategorySerializer
from .serializers import BookListSerializer, BookFilialSerializer, OrderItemSerializer, FilialSerializer, \
    BookFilialCreateSerializer


class BookListAPIView(ListAPIView):
    serializer_class = BookListSerializer

    def get_queryset(self):
        get = self.request.GET
        filters = {}

        # self.test_books()

        if get.get("code"):
            filters["code"] = get.get("code")
        if get.get("title"):
            filters["title__contains"] = get.get("title")
        if get.get("category"):
            filters["categories__name"] = get.get("category")

        p = Paginator(Book.objects.filter(**filters), get.get("count", 9))

        return p.page(get.get("page", 1)).object_list

    # def test_books(self):
    #     c = Category.objects.all().last()
    #     b = Book.objects.first()
    #
    #     for i in range(100):
    #         tb = Book(
    #             title=f"test-{i}",
    #             code=f"{i}",
    #             description=f"test-desc-{i}",
    #             album=b.album
    #         )
    #         tb.save()
    #         tb.categories.add(c)


class GetPagesNumber(APIView):
    def get(self, request):
        get = self.request.GET
        filters = {}

        # self.test_books()

        if get.get("code"):
            filters["code"] = get.get("code")
        if get.get("title"):
            filters["title__contains"] = get.get("title")
        if get.get("category"):
            filters["categories__name"] = get.get("category")

        p = Paginator(Book.objects.filter(**filters), get.get("count", 9))

        return Response(p.num_pages)


class BookFilialListAPIView(ListAPIView):
    serializer_class = BookFilialSerializer

    def get_queryset(self):
        get = self.request.GET
        filters = {"book_id": get.get("book")}

        return BookFilial.objects.filter(**filters).order_by("price")


class BookedBookFilialAPIView(ListAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        get = self.request.GET
        vendor = Vendor.objects.get(user_id=self.request.user.pk)
        print(vendor)

        book_filials = OrderItem.objects.exclude(
            token=None
        ).filter(
            # token__creation_date__lt=timezone.now()-timedelta(days=1),
            book_filial__filial__vendor_id=vendor.pk
        )

        return book_filials


class FilialCreateApiView(APIView):
    def post(self, request):
        serializers = FilialSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class FilialListApiView(APIView):
    def get(self,  request):
        filial = Filial.objects.filter(
            vendor__user_id=request.user.pk
        )
        serializers = FilialSerializer(filial, many=True)
        return Response(serializers.data)


class FilialUpdateApiView(APIView):

    def get_object(self, id):
        try:
            return Filial.objects.get(id=id)
        except Filial.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        post = self.get_object(id)
        serializer = FilialSerializer(post, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilialDestroyApiView(APIView):

    def get_object(self, id):
        try:
            return Filial.objects.get(id=id)
        except Filial.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookFilialCreateAPIView(CreateAPIView):
    queryset = BookFilial.objects.all()
    serializer_class = BookFilialCreateSerializer
