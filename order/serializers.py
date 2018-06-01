import requests
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from book.serializers import RoomSerializer
from customer.serializers import CouponCodeSerializer
from mall.serializers import ProductSerializer
from order.models import Order
from shop.fields import CurrentShopDefault


class OrderSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())
    use_coupon = CouponCodeSerializer(read_only=True)
    rooms = RoomSerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'shop', 'customer_id', 'category', 'order_number', 'price', 'status', 'full_name', 'mobile', 'remark',
                  'use_balance', 'use_coupon', 'use_wx', 'starts_at', 'ends_at', 'arrive', 'days', 'rooms', 'products']
        read_only_fields = ['customer_id', 'category', 'order_number', 'price', 'status', 'use_balance', 'use_coupon', 'use_wx']
