import requests
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from book.models import Room, Order
from customer.serializers import CouponCodeSerializer
from shop.fields import CurrentShopDefault


class RoomSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())

    class Meta:
        model = Room
        fields = ['id', 'shop', 'name', 'description', 'pic',
                  'area', 'bed_type', 'window', 'bed_width', 'capacity', 'floor',
                  'price']


class OrderSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())
    use_coupon = CouponCodeSerializer(read_only=True)
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'shop', 'category', 'order_number', 'price', 'status', 'full_name', 'mobile', 'remark',
                  'use_balance', 'use_coupon', 'use_wx', 'starts_at', 'ends_at', 'arrive', 'days', 'rooms']
        read_only_fields = ['category', 'order_number', 'price', 'status', 'use_balance', 'use_coupon', 'use_wx',
                            'starts_at', 'ends_at', 'arrive']
