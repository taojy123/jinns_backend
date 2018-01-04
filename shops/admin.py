from django.contrib import admin

from shops import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop_id', 'name']
    search_fields = ['name']


@admin.register(models.ShopToken)
class ShopTokenAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'access_token', 'refresh_token', 'scope', 'expires_in']
    search_fields = ['shop__name']
    raw_id_fields = ['shop']


