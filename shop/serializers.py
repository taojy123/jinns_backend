from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from customer.models import BalanceHistory
from customer.serializers import CustomerSerializer
from shop.models import Shop, ShopPic, Coupon


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['id', 'name', 'address', 'phone', 'location', 'score', 'reviews_count', 'pic', 'pics']


class ShopPicSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopPic
        fields = ['id', 'pic', 'position']


class BalanceHistorySerializer(serializers.ModelSerializer):

    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = BalanceHistory
        fields = ['id', 'customer', 'amount', 'reason']


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = ['id', 'name', 'price']


