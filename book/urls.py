from django.conf.urls import url, include
from rest_framework import routers

from book.views import RoomViewSet

router = routers.DefaultRouter()

router.register(r'rooms', RoomViewSet, base_name='rooms')

urlpatterns = [
    url(r'^', include(router.urls)),
]
