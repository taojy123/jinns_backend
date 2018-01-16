
from rest_framework import generics, response, exceptions, viewsets

from customer.models import Customer, CouponCode
from customer.permissions import IsCustomerOwner
from customer.serializers import CustomerSerializer, CouponCodeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsCustomerOwner]
    pagination_class = None

    def get_queryset(self):
        return Customer.objects.filter(id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CouponCodeViewSet(viewsets.ModelViewSet):
    serializer_class = CouponCodeSerializer
    permission_classes = [IsCustomerOwner]
    pagination_class = None

    def get_queryset(self):
        return CouponCode.objects.filter(customer=self.request.user)


