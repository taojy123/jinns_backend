from django.conf.urls import url, include
from rest_framework import routers

from shop.views import GenerateTokenView, ShopViewSet, ShopPicViewSet, CouponViewSet, QiniuUptokenView, CustomerViewSet

router = routers.DefaultRouter()


router.register(r'shops', ShopViewSet, base_name='shops')
router.register(r'shop_pics', ShopPicViewSet, base_name='shop_pics')
router.register(r'customers', CustomerViewSet, base_name='customers')
router.register(r'coupons', CouponViewSet, base_name='coupons')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^oauth/token/$', GenerateTokenView.as_view(), name='generate_token'),
    url(r'^qiniu/uptoken/$', QiniuUptokenView.as_view(), name='qiniu_uptoken'),
]
