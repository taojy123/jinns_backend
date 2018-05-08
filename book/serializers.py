import requests
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from book.models import Room
from shop.fields import CurrentShopDefault


class RoomSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())

    class Meta:
        model = Room
        fields = ['id', 'shop', 'name', 'description', 'pic', 'price', 'quantity',
                  'area', 'bed_type', 'window', 'bed_width', 'capacity', 'floor',
                  'pics']


