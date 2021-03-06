import uuid

from django.db import models
from jinns.models import Model

import logging

from jinns.utils import make_token

logger = logging.getLogger('apps')


class Shop(Model):

    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    pic = models.CharField(max_length=500, blank=True, help_text='主图')
    location = models.CharField(max_length=255, blank=True, help_text='坐标定位: 120.23,38.92')
    token = models.CharField(max_length=255, default=make_token)

    @property
    def score(self):
        return 5

    @property
    def reviews_count(self):
        return 1000

    @property
    def pics(self):
        return [self.pic] * 3

    def __str__(self):
        return self.name


class ShopPic(Model):

    shop = models.ForeignKey(Shop)
    pic = models.CharField(max_length=500, blank=True)
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.pic


class Coupon(Model):

    shop = models.ForeignKey(Shop)
    name = models.CharField(max_length=255, blank=True)
    price = models.FloatField(default=10)

    def __str__(self):
        return self.name

