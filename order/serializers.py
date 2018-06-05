import requests
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from book.serializers import RoomSerializer
from customer.serializers import CouponCodeSerializer
from mall.serializers import ProductSerializer
from order.models import Order, OrderRoom, OrderProduct
from shop.fields import CurrentShopDefault


class OrderRoomSerializer(serializers.ModelSerializer):

    room = RoomSerializer(read_only=True)

    class Meta:
        model = OrderRoom
        fields = ['id', 'order_id', 'room', 'quantity']
        read_only_fields = ['order_id', 'quantity']


class OrderProductSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['id', 'order_id', 'product', 'quantity']
        read_only_fields = ['order_id', 'quantity']


class OrderSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())
    use_coupon = CouponCodeSerializer(read_only=True)
    order_rooms = OrderRoomSerializer(many=True, read_only=True)
    order_products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'shop', 'customer_id', 'category', 'order_number', 'price', 'status', 'get_status_display', 'full_name', 'mobile', 'remark',
                  'use_balance', 'use_coupon', 'use_wx', 'starts_at', 'ends_at', 'arrive', 'days', 'order_rooms','order_products',
                  'created_at', 'updated_at']
        read_only_fields = ['customer_id', 'category', 'order_number', 'price', 'status', 'use_balance', 'use_coupon', 'use_wx']
