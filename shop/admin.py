from django.contrib import admin

from shop import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'address', 'phone', 'location', 'score', 'reviews_count']
    search_fields = ['name']


@admin.register(models.ShopPic)
class ShopPicAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'pic', 'position']
    raw_id_fields = ['shop']
    list_filter = ['shop']


