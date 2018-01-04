from django.conf.urls import url, include
from rest_framework import routers

from event.views import EventViewSet

router = routers.DefaultRouter()

router.register(r'event', EventViewSet, base_name='event')

urlpatterns = [
    url(r'^', include(router.urls)),
]
