import datetime
from django.apps import apps

from jinns.celery import celery_app
from jinns.utils import shop_api_request


@celery_app.task
def daily_task():
    pass


