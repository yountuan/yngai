from django.http import Http404
from rest_framework import permissions, status, generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
# from django_filters.rest_framework import DjangoFilterBackend
# from account.permissions import IsVendor, IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet

from base.models import Book, Category, Filial
from book.serializers import BookSerializer, CategorySerializer, FilialSerializer
from base.models import Book, Category
from book.serializers import BookSerializer, CategorySerializer

class BookCreateApiView(APIView):

    def post(self, request):
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BookListSerializer(APIView):

    def get(self,  request):
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True)
        return Response(serializers.data)


class BookUpdateApiView(APIView):

    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        post = self.get_object(id)
        serializer = BookSerializer(post, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDestroyApiView(APIView):

    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryCreateApiView(APIView):

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)

class CategoryUpdateApiView(APIView):

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        post = self.get_object(id)
        serializer = CategorySerializer(post, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDestroyApiView(APIView):
    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#
# class CartCreateAPIView(APIView):
#     permission_classes = [IsVendor]
#
#     def post(self, request):
#         serializers = CartSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class GetCartAPIView(APIView):
#     permission_classes = [IsOwnerOrReadOnly]
#     parser_classes = [JSONParser]
#
#     def get(self, request, id):
#         cart = Cart.objects.get(user_id=id)
#         product = cart.product.all()
#         serializer = CartSerializer(cart)
#         serializer2 = ProductSerializer(product, many=True)
#         data = serializer.data
#         data['product'] = serializer2.data
#         return Response(data)
#
#     def put(self, requests,id):
#         cart = Cart.objects.get(user_id=id)
#         serializer = UpdateSerializer(cart, data=requests.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductFilterApiView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['category', 'name', 'price']