import requests
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from mall.models import Product
from shop.fields import CurrentShopDefault


class ProductSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())

    class Meta:
        model = Product
        fields = ['id', 'shop', 'name', 'description', 'pic', 'price']


