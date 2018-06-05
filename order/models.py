import random

from django.db import models
from django.utils import timezone

from book.models import Room
from jinns.models import Model

import logging

from mall.models import Product

logger = logging.getLogger('apps')


def make_order_number():
    # 18 位订单编号
    now = timezone.localtime(timezone.now()).strftime('%Y%m%d%H%M%S')
    return now + str(random.randint(1000, 9999))


class Order(Model):

    CATEGORY_CHOICES = (
        ('room', '订房'),
        ('mall', '商城'),
    )

    STATUS_CHOICES = (
        ('pending', '待支付'),
        ('paid', '已支付'),
        ('refunding', '退款中'),
        ('refund', '已退款'),
        ('cancel', '已取消'),  # 未支付的订单
    )

    shop = models.ForeignKey('shop.Shop')
    customer = models.ForeignKey('customer.Customer', blank=True, null=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='room')
    order_number = models.CharField(max_length=255, default=make_order_number, help_text='订单号')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    price = models.FloatField(default=0, help_text='订单总价 单位元')

    full_name = models.CharField(max_length=255, blank=True, help_text='姓名')
    mobile = models.CharField(max_length=255, blank=True, help_text='手机')
    remark = models.TextField(blank=True, help_text='备注')

    # 支付信息
    use_balance = models.FloatField(default=0)
    use_coupon = models.ForeignKey('customer.CouponCode', blank=True, null=True)
    use_wx = models.FloatField(default=0)

    # 订房订单
    starts_at = models.DateField(null=True, blank=True)
    ends_at = models.DateField(null=True, blank=True)
    arrive = models.CharField(max_length=255, blank=True, help_text='到店时间')

    @property
    def days(self):
        return (self.ends_at - self.starts_at).days

    @property
    def rooms(self):
        room_ids = self.orderroom_set.all().values_list('room_id', flat=True)
        return Room.objects.filter(id__in=room_ids)

    @property
    def products(self):
        product_ids = self.orderproduct_set.all().values_list('product_id', flat=True)
        return Product.objects.filter(id__in=product_ids)

    @property
    def order_rooms(self):
        return self.orderroom_set.all()

    @property
    def order_products(self):
        return self.orderproduct_set.all()

    @property
    def title(self):
        r = ''
        for item in self.orderroom_set.all():
            r += item.name
            if item.quantity > 1:
                r += '* %d' % item.quantity
            r += ', '
        for item in self.orderproduct_set.all():
            r += item.name
            if item.quantity > 1:
                r += '* %d' % item.quantity
            r += ', '
        return r.strip(', ')

    @property
    def pic(self):
        items = list(self.rooms) or list(self.products)
        if items:
            return items[0].pic
        return ''

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = timezone.now().strftime('%Y%m%d%D%M%S') + str(random.randint(10, 99))
        return super().save(*args, **kwargs)

    def calculate_total_price(self, need_save=False):
        total_price = 0
        for item in self.orderroom_set.all():
            if not item.room:
                continue
            total_price += item.room.price * item.quantity
        for item in self.orderproduct_set.all():
            if not item.product:
                continue
            total_price += item.product.price * item.quantity
        self.price = total_price
        if need_save:
            self.save()
        return total_price


class OrderRoom(Model):
    order = models.ForeignKey(Order)
    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)


class OrderProduct(Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
