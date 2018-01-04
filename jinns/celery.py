from __future__ import absolute_import
import os

from celery import Celery, platforms
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jinns.settings')

platforms.C_FORCE_ROOT = True

celery_app = Celery('jinns')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(settings.INSTALLED_APPS)


@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

