import requests
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from mall.models import Product, Banner
from shop.fields import CurrentShopDefault


class BannerSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())

    class Meta:
        model = Banner
        fields = ['id', 'shop', 'pic', 'position']


class ProductSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())

    class Meta:
        model = Product
        fields = ['id', 'shop', 'name', 'price', 'pic', 'description', 'description_pic', 'is_hot', 'hot_pic']


