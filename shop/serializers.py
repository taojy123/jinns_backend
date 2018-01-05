from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from shop.models import Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['id', 'name', 'address', 'phone', 'location', 'score', 'reviews_count']


