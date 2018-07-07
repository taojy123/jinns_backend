
from django_filters import rest_framework as filters, STRICTNESS
from rest_framework import viewsets

from book.models import Room
from book.serializers import RoomSerializer


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
    filter_class = RoomFilter

    def get_queryset(self):
        return Room.objects.filter(shop=self.request.shop)


