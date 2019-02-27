import uuid

from django.db import models
from django.db.models import Sum

from jinns.models import Model

import logging

from jinns.utils import make_token

logger = logging.getLogger('apps')


class Customer(Model):

    shop = models.ForeignKey('shop.Shop')
    full_name = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    token = models.CharField(max_length=255, default=make_token)

    # wx
    openid = models.CharField(max_length=255, blank=True)
    nickname = models.CharField(max_length=255, blank=True)
    headimgurl = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.full_name

    @property
    def balance(self):
        return self.balancehistory_set.all().aggregate(Sum('amount')).get('amount__sum') or 0

    @property
    def point(self):
        return self.pointhistory_set.all().aggregate(Sum('amount')).get('amount__sum') or 0


class PointHistory(Model):

    customer = models.ForeignKey(Customer)
    amount = models.IntegerField(default=0)
    reason = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.reason


class BalanceHistory(Model):

    customer = models.ForeignKey(Customer)
    amount = models.FloatField(default=0)
    reason = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.reason


class CouponCode(Model):

    coupon = models.ForeignKey('shop.Coupon')
    customer = models.ForeignKey(Customer)

    @property
    def is_used(self):
        return self.order_set.all().exists()

    def __str__(self):
        return self.coupon.name


