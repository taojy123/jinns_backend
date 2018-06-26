from django.conf.urls import url, include
from rest_framework import routers

from customer.views import CustomerViewSet, CouponCodeViewSet, OrderViewSet, GetCustomerTokenView

router = routers.DefaultRouter()

# apis for customer
router.register(r'customers', CustomerViewSet, base_name='customers')
router.register(r'coupon_codes', CouponCodeViewSet, base_name='coupon_codes')
router.register(r'orders', OrderViewSet, base_name='orders')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^oauth/token/$', GetCustomerTokenView.as_view(), name='get_customer_token'),
]
