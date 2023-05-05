from rest_framework import serializers
from base.models import Book, Category, BookFilial, OrderItem, Filial


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", ]


class BookListSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "title", "description", "code", "album", "categories"]

    def get_categories(self, obj: Book):
        return CategorySerializer(obj.categories.all(), many=True).data


class BookFilialSerializer(serializers.ModelSerializer):
    book = BookListSerializer(many=False)
    filial = serializers.CharField(source="filial.address")

    class Meta:
        model = BookFilial
        fields = ["id", "book", "filial", "quantity", "price"]


class OrderItemSerializer(serializers.ModelSerializer):
    book_filial = BookFilialSerializer(many=False)
    token = serializers.CharField(source="token.token")
    client = serializers.CharField(source="token.client.user.username")

    class Meta:
        model = OrderItem
        fields = ["book_filial", "quantity", "price", "token", "client"]


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = ['id', 'vendor', 'schedule', 'address']


class BookFilialCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFilial
        fields = ['book', 'filial', 'quantity', 'price']
