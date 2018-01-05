import hashlib
import json

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django_filters import rest_framework as filters, STRICTNESS
from rest_framework import viewsets, mixins, generics, exceptions, response
from rest_framework.viewsets import ReadOnlyModelViewSet

from jinns.utils import shop_api_request, get_shop_by_domain
from book.models import Room
from book.serializers import RoomSerializer
from shop.models import Shop
from shop.permissions import HasShopDomain

import logging


logger = logging.getLogger('apps')


class RoomFilter(filters.FilterSet):

    order_by = filters.OrderingFilter(fields=['id'])

    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        strict = STRICTNESS.IGNORE
        model = Room
        fields = {
            'id': ['exact', 'in'],
        }


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [HasShopDomain]
    filter_class = RoomFilter
    pagination_class = None

    def get_queryset(self):
        shop = get_shop_by_domain(self.request.shop_domain)
        return Room.objects.filter(shop=shop)


