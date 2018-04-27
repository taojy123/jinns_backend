from django.contrib import admin

from mall import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'name', 'price']
    raw_id_fields = ['shop']
    search_fields = ['name']
    list_filter = ['shop']

