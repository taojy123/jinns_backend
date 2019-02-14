from django.contrib import admin

from mall import models


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'pic', 'position']
    raw_id_fields = ['shop']
    list_filter = ['shop']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'name', 'price', 'is_hot']
    raw_id_fields = ['shop']
    search_fields = ['name']
    list_filter = ['shop']

