import uuid

from django.db import models
from jinns.models import Model

import logging
logger = logging.getLogger('apps')


def make_token():
    return uuid.uuid4().hex


class Shop(Model):

    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True, help_text='坐标定位: 120.23,38.92')
    token = models.CharField(max_length=255, default=make_token)

    @property
    def score(self):
        return 5

    @property
    def reviews_count(self):
        return 1000

    def __str__(self):
        return self.name


class ShopPic(models.Model):

    shop = models.ForeignKey(Shop)
    pic = models.ImageField(upload_to='shop_pic')
    position = models.IntegerField(default=0)




