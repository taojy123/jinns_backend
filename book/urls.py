from django.conf.urls import url, include
from rest_framework import routers

from book.views import RoomViewSet

router = routers.DefaultRouter()

router.register(r'room', RoomViewSet, base_name='room')

urlpatterns = [
    url(r'^', include(router.urls)),
]
