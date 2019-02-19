
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_filters import rest_framework as filters, STRICTNESS
from rest_framework import viewsets, mixins, generics, exceptions, response
from rest_framework.viewsets import ReadOnlyModelViewSet


from mall.models import Product, Banner
from mall.serializers import ProductSerializer, BannerSerializer
from shop.models import Shop

import logging


logger = logging.getLogger('apps')


class BannerViewSet(viewsets.ModelViewSet):
    serializer_class = BannerSerializer

    def get_queryset(self):
        return Banner.objects.filter(shop=self.request.shop)


class ProductFilter(filters.FilterSet):

    order_by = filters.OrderingFilter(fields=['id', 'is_hot', 'name'])

    class Meta:
        strict = STRICTNESS.RETURN_NO_RESULTS
        model = Product
        fields = {
            'id': ['exact', 'in'],
            'is_hot': ['exact'],
        }


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_class = ProductFilter

    def get_queryset(self):
        return Product.objects.filter(shop=self.request.shop)


