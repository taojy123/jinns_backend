from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from shop.models import Shop, ShopPic, Coupon


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['id', 'name', 'address', 'phone', 'location', 'score', 'reviews_count']


class ShopPicSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopPic
        fields = ['id', 'pic', 'position']


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = ['id', 'name', 'price']


