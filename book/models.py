import random

from django.db import models
from django.utils import timezone

from jinns.models import Model

import logging
logger = logging.getLogger('apps')


def make_order_number():
    # 18 位订单编号
    now = timezone.localtime(timezone.now()).strftime('%Y%m%d%H%M%S')
    return now + str(random.randint(1000, 9999))


class Room(Model):

    shop = models.ForeignKey('shop.Shop')
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    pic = models.CharField(max_length=500, blank=True)
    price = models.FloatField(default=100)
    quantity = models.IntegerField(default=5)
    area = models.CharField(max_length=255, blank=True, help_text='面积')
    bed_type = models.CharField(max_length=255, blank=True, help_text='床型')
    window = models.CharField(max_length=255, blank=True, help_text='窗户')
    bed_width = models.CharField(max_length=255, blank=True, help_text='床宽')
    capacity = models.CharField(max_length=255, blank=True, help_text='入住人数')
    floor = models.CharField(max_length=255, blank=True, help_text='所在楼层')

    def __str__(self):
        return self.name


