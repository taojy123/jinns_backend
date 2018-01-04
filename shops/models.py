import requests
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from jsonfield import JSONField

import logging


logger = logging.getLogger('apps')


class Shop(models.Model):

    name = models.CharField(max_length=100, unique=True)
    shop_id = models.IntegerField(default=0)

    metafield = JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ShopToken(models.Model):

    shop = models.ForeignKey(Shop)
    access_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    scope = models.CharField(max_length=500)
    expires_in = models.IntegerField(default=0)

    metafield = JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

