from django.conf.urls import url, include
from rest_framework import routers

from customer.views import CustomerViewSet, CouponCodeViewSet

router = routers.DefaultRouter()

router.register(r'customers', CustomerViewSet, base_name='customers')
router.register(r'coupon_codes', CouponCodeViewSet, base_name='coupon_codes')


urlpatterns = [
    url(r'^', include(router.urls)),
]
