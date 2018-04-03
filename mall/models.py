import random

from django.db import models
from django.utils import timezone

from jinns.models import Model

import logging
logger = logging.getLogger('apps')


class Product(Model):

    shop = models.ForeignKey('shop.Shop')
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    pic = models.ImageField(upload_to='product_pic')
    price = models.FloatField(default=100)

    def __str__(self):
        return self.name



