import qiniu
from django.conf import settings
from rest_framework import generics, response, exceptions, viewsets
from rest_framework.decorators import detail_route
from django_filters import rest_framework as filters, STRICTNESS


from customer.models import Customer, BalanceHistory
from customer.serializers import CustomerSerializer
from shop.models import Shop, ShopPic, Coupon
from shop.serializers import ShopSerializer, ShopPicSerializer, CouponSerializer, BalanceHistorySerializer


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer

    def get_queryset(self):
        return Shop.objects.filter(id=self.request.shop.id)

    def get_object(self):
        return self.get_queryset().get()

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ShopPicViewSet(viewsets.ModelViewSet):
    serializer_class = ShopPicSerializer

    def get_queryset(self):
        return ShopPic.objects.filter(shop=self.request.shop)


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.filter(shop=self.request.shop)

    @detail_route(methods=['post'])
    def set_balance(self, request, *args, **kwargs):
        customer = self.get_object()
        amount = request.data.get('amount', 0)
        reason = request.data.get('reason', '')
        customer.balancehistory_set.create(amount=amount, reason=reason)
        return response.Response(self.get_serializer(customer).data)


class BalanceHistoryFilter(filters.FilterSet):

    order_by = filters.BalanceHistoryingFilter(fields=['id', 'created_at'])

    class Meta:
        strict = STRICTNESS.RETURN_NO_RESULTS
        model = BalanceHistory
        fields = {
            'id': ['exact', 'in'],
            'customer': ['exact', 'in'],
            'created_at': ['gte', 'lte'],
        }


class BalanceHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = BalanceHistorySerializer
    filter_class = BalanceHistoryFilter

    def get_queryset(self):
        return BalanceHistory.objects.filter(shop=self.request.shop)


class CouponViewSet(viewsets.ModelViewSet):
    serializer_class = CouponSerializer

    def get_queryset(self):
        return Coupon.objects.filter(shop=self.request.shop)


class GenerateTokenView(generics.GenericAPIView):
    serializer_class = ShopSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        code = request.data.get('code')
        shop_domain = request.data.get('shop')
        return response.Response()


class QiniuUptokenView(generics.GenericAPIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        access_key = settings.QINIU_ACCESS_KEY
        secret_key = settings.QINIU_SECRET_KEY
        bucket = settings.QINIU_BUCKET_NAME
        q = qiniu.Auth(access_key, secret_key)
        token = q.upload_token(bucket, expires=3600 * 24 * 30)
        return response.Response({
            'uptoken': token,
            'expires_in': 3600 * 24 * 30
        })

