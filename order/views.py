from django.db.models import Q
from rest_framework import viewsets, mixins, generics, exceptions, response
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters import rest_framework as filters, STRICTNESS
from order.models import Order
from order.serializers import OrderSerializer
from shop.models import Shop

import logging


logger = logging.getLogger('apps')


class OrderFilter(filters.FilterSet):

    order_by = filters.OrderingFilter(fields=['id', 'starts_at', 'created_at', 'updated_at'])

    keyword = filters.CharFilter(method='filter_keyword')

    def filter_keyword(self, queryset, name, value):

        if not value:
            return queryset

        q1 = Q(order_number__icontains=value)
        q2 = Q(full_name__icontains=value)
        q3 = Q(mobile=value)
        queryset = queryset.filter(q1 | q2 | q3)

        return queryset

    class Meta:
        strict = STRICTNESS.RETURN_NO_RESULTS
        model = Order
        fields = {
            'id': ['exact', 'in'],
            'category': ['exact', 'in'],
            'status': ['exact', 'in'],
            'order_number': ['exact', 'icontains'],
            'starts_at': ['gte', 'lte'],
            'ends_at': ['gte', 'lte'],
        }


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    filter_class = OrderFilter

    def get_queryset(self):
        return Order.objects.filter(shop=self.request.shop)


