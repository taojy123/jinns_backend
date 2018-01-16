from rest_framework import exceptions
from rest_framework.permissions import BasePermission, SAFE_METHODS

from customer.models import Customer
from shop.models import Shop


class IsAuthenticatedCustomer(BasePermission):

    def has_permission(self, request, view):
        return isinstance(request.user, Customer)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsCustomerOwner(IsAuthenticatedCustomer):

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'customer') and request.user != obj.customer and obj.customer:
            return False
        return super(IsCustomerOwner, self).has_object_permission(request, view, obj)


class IsCustomerOwnerOrReadOnly(IsCustomerOwner):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return super(IsCustomerOwnerOrReadOnly, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return super(IsCustomerOwnerOrReadOnly, self).has_object_permission(request, view, obj)


