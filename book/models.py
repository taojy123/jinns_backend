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
    pic = models.ImageField(upload_to='room_pic')
    area = models.CharField(max_length=255, blank=True, help_text='面积')
    bed_type = models.CharField(max_length=255, blank=True, help_text='床型')
    window = models.CharField(max_length=255, blank=True, help_text='窗户')
    bed_width = models.CharField(max_length=255, blank=True, help_text='床宽')
    capacity = models.CharField(max_length=255, blank=True, help_text='入住人数')
    floor = models.CharField(max_length=255, blank=True, help_text='所在楼层')
    price = models.FloatField(default=100)

    def __str__(self):
        return self.name


class Order(Model):

    CATEGORY_CHOICES = (
        ('room', '订房'),
    )

    STATUS_CHOICES = (
        ('pending', '待支付'),
        ('paid', '已支付'),
        ('refunding', '退款中'),
        ('refund', '已退款'),
        ('cancel', '已取消'),  # 长时间未支付的订单
    )

    shop = models.ForeignKey('shop.Shop')
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='room')
    order_number = models.CharField(max_length=255, default=make_order_number, help_text='订单号')
    price = models.FloatField(help_text='订单总价 单位元')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')

    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.SET_NULL)
    starts_at = models.DateField(null=True, blank=True)
    ends_at = models.DateField(null=True, blank=True)

    @property
    def days(self):
        return (self.ends_at - self.starts_at).days



