from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from customer.models import CouponCode, Customer
from shop.fields import CurrentShopDefault
from shop.serializers import CouponSerializer


class CustomerSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())

    class Meta:
        model = Customer
        fields = ['id', 'shop', 'full_name', 'mobile', 'balance', 'point', 'openid', 'nickname', 'headimgurl']


class CouponCodeSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())
    coupon = CouponSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = CouponCode
        fields = ['id', 'shop', 'coupon', 'customer', 'is_used']
