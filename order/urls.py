from django.conf.urls import url, include
from rest_framework import routers

from order.views import OrderViewSet

router = routers.DefaultRouter()

router.register(r'orders', OrderViewSet, base_name='orders')

urlpatterns = [
    url(r'^', include(router.urls)),
]
