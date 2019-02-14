from django.conf.urls import url, include
from rest_framework import routers

from mall.views import ProductViewSet, BannerViewSet

router = routers.DefaultRouter()

router.register(r'banners', BannerViewSet, base_name='banners')
router.register(r'products', ProductViewSet, base_name='products')

urlpatterns = [
    url(r'^', include(router.urls)),
]
