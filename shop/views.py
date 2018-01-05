
from rest_framework import generics, response, exceptions
from shop.serializers import ShopSerializer


class GenerateTokenView(generics.GenericAPIView):
    serializer_class = ShopSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        code = request.data.get('code')
        shop_domain = request.data.get('shop')
        return response.Response()


