from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from shops.models import Shop, ShopToken


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['id', 'name', 'domain', 'shop_id']


class ShopTokenSerializer(serializers.ModelSerializer):

    shop = ShopSerializer(read_only=True)

    class Meta:
        model = ShopToken
        fields = ['id', 'shop', 'access_token', 'refresh_token', 'scope', 'expires_in']

