from django.conf.urls import url, include
from rest_framework import routers

from book.views import RoomViewSet, OrderViewSet

router = routers.DefaultRouter()

router.register(r'rooms', RoomViewSet, base_name='rooms')
router.register(r'orders', OrderViewSet, base_name='orders')

urlpatterns = [
    url(r'^', include(router.urls)),
]
