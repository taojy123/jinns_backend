import random

from django.db import models
from django.utils import timezone

from jinns.models import Model

import logging
logger = logging.getLogger('apps')


class Banner(Model):

    shop = models.ForeignKey('shop.Shop')
    pic = models.CharField(max_length=500, blank=True)
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.pic


class Product(Model):

    shop = models.ForeignKey('shop.Shop')

    name = models.CharField(max_length=255, blank=True)
    price = models.FloatField(default=100)
    pic = models.CharField(max_length=500, blank=True, help_text='主图')

    description = models.TextField(blank=True)
    description_pic = models.CharField(max_length=500, blank=True, help_text='详情图')

    is_hot = models.BooleanField(default=False, help_text='是否热卖')
    hot_pic = models.CharField(max_length=500, blank=True, help_text='热卖图')

    def __str__(self):
        return self.name

