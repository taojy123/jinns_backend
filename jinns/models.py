
from django.db import models
from jsonfield import JSONField

import logging
logger = logging.getLogger('apps')


class Model(models.Model):

    metafield = JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

