from django.contrib import admin

from mall import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'name', 'price']
    raw_id_fields = ['shop']
    search_fields = ['name']
    list_filter = ['shop']


@admin.register(models.OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'order', 'product', 'quantity']
    raw_id_fields = ['order', 'product']



