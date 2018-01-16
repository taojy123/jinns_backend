from django.contrib import admin

from customer import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ['id', 'shop', 'full_name', 'mobile', 'balance', 'openid', 'nickname', 'headimgurl']
    raw_id_fields = ['shop']
    list_filter = ['shop']


@admin.register(models.CouponCode)
class CouponCodeAdmin(admin.ModelAdmin):

    list_display = ['id', 'coupon', 'customer']
    raw_id_fields = ['coupon', 'customer']
    list_filter = ['coupon', 'customer']
