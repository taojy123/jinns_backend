from django.contrib import admin

from book import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'name', 'price']
    raw_id_fields = ['shop']
    search_fields = ['name']
    list_filter = ['shop']


