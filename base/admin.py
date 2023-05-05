from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class FilialItemInline(admin.TabularInline):
    model = Filial


class AdminCartToken(admin.ModelAdmin):
    inlines = [OrderItemInline]


class AdminVendor(admin.ModelAdmin):
    inlines = [FilialItemInline]


admin.site.register(Vendor, AdminVendor)
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BookFilial)
admin.site.register(Filial)
admin.site.register(CartToken, AdminCartToken)
admin.site.register(OrderItem)
