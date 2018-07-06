
from rest_framework import viewsets, mixins, generics, exceptions, response
from rest_framework.viewsets import ReadOnlyModelViewSet

from order.models import Order
from order.serializers import OrderSerializer
from shop.models import Shop

import logging


logger = logging.getLogger('apps')


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    pagination_class = None

    def get_queryset(self):
        return Order.objects.filter(shop=self.request.shop)


