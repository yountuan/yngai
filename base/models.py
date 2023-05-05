from django.db import models
from django.contrib.auth import get_user_model

from django.utils.crypto import get_random_string

User = get_user_model()


class Vendor(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    company_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=80)

    def __str__(self):
        return self.company_name


class Category(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    description = models.TextField()
    code = models.CharField(max_length=50)
    album = models.ImageField()

    def __str__(self):
        return self.title


class Client(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=80)
    # avatar = models.ImageField(default='default.jpg', upload_to='post_image/')

    def __str__(self):
        return self.user.username


class Filial(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    schedule = models.TextField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address


class BookFilial(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    filial = models.ForeignKey(Filial, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.filial.vendor.company_name} >> {self.filial.address}: {self.book.title} X {self.quantity}"


class CartToken(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=50, default=get_random_string(50))

    @staticmethod
    def validate_token(token):
        return CartToken.objects.filter(token=token).exists()

    def __str__(self):
        return f"{self.client.user.username}: {self.creation_date}"


class OrderItem(models.Model):
    token = models.ForeignKey(CartToken, null=True, on_delete=models.SET_NULL)
    book_filial = models.ForeignKey(BookFilial, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.token.client.user.username}: {self.book_filial.book.title} X {self.quantity}"


class Payment(models.Model):
    data = models.JSONField()

class Delivery(models.Model):
    data = models.JSONField()