from rest_framework import serializers
from base.models import Book, Category, Filial


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'categories', 'description', 'code', 'album']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image']


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = ["schedule", "address", "vendor"]