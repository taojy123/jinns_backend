import requests
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers, exceptions

from event.models import Event
from shops.fields import CurrentShopDefault


class EventSerializer(serializers.ModelSerializer):

    shop = serializers.HiddenField(default=CurrentShopDefault())

    class Meta:
        model = Event
        fields = ['id']


