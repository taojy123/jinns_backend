from django.contrib import admin

from book import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'name', 'price']
    raw_id_fields = ['shop']
    search_fields = ['name']
    list_filter = ['shop']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'category', 'order_number', 'price', 'status']
    raw_id_fields = ['shop']
    search_fields = ['order_number']
    list_filter = ['shop', 'status']


@admin.register(models.OrderRoom)
class OrderRoomAdmin(admin.ModelAdmin):

    list_display = ['id', 'order', 'room', 'quantity']
    raw_id_fields = ['order', 'room']


