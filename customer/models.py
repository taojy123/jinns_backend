import uuid

from django.db import models
from jinns.models import Model

import logging
logger = logging.getLogger('apps')


class Customer(Model):

    shop = models.ForeignKey('shop.Shop')
    full_name = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    balance = models.FloatField(default=0, help_text='账户余额')

    # wx
    openid = models.CharField(max_length=255, blank=True)
    nickname = models.CharField(max_length=255, blank=True)
    headimgurl = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.full_name


class CouponCode(Model):

    coupon = models.ForeignKey('shop.Coupon')
    customer = models.ForeignKey(Customer)

    @property
    def is_used(self):
        return self.order_set.all().exists()

    def __str__(self):
        return self.coupon.name


