
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, mixins, generics, exceptions, response
from rest_framework.viewsets import ReadOnlyModelViewSet

from jinns.utils import shop_api_request, get_shop_by_domain
from mall.models import Product
from mall.serializers import ProductSerializer
from shop.models import Shop

import logging


logger = logging.getLogger('apps')


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = None

    def get_queryset(self):
        return Product.objects.filter(shop=self.request.shop)


