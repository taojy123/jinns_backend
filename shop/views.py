
from rest_framework import generics, response, exceptions, viewsets

from shop.models import Shop, ShopPic, Coupon
from shop.serializers import ShopSerializer, ShopPicSerializer, CouponSerializer


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    pagination_class = None

    def get_queryset(self):
        return Shop.objects.filter(id=self.request.shop.id)

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ShopPicViewSet(viewsets.ModelViewSet):
    serializer_class = ShopPicSerializer
    pagination_class = None

    def get_queryset(self):
        return ShopPic.objects.filter(shop=self.request.shop)


class CouponViewSet(viewsets.ModelViewSet):
    serializer_class = CouponSerializer
    pagination_class = None

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


