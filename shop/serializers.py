from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from customer.models import BalanceHistory, Customer
from shop.models import Shop, ShopPic, Coupon


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['id', 'name', 'address', 'phone', 'location', 'score', 'reviews_count', 'pic', 'pics']


class ShopPicSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopPic
        fields = ['id', 'pic', 'position']


class CustomerSerializer(serializers.ModelSerializer):

    shop_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'shop_id', 'full_name', 'mobile', 'balance', 'points', 'openid', 'nickname', 'headimgurl']


class BalanceHistorySerializer(serializers.ModelSerializer):

    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = BalanceHistory
        fields = ['id', 'customer', 'amount', 'reason']


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = ['id', 'name', 'price']


