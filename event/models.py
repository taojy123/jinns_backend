import datetime
import requests
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F, Sum
from django.utils import timezone
from jsonfield import JSONField

from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    shop = models.ForeignKey('shops.Shop')

    metafield = JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

