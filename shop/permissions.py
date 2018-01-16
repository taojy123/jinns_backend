from rest_framework import exceptions
from rest_framework.permissions import BasePermission, SAFE_METHODS

from customer.models import Customer
from shop.models import Shop


class IsAuthenticatedShop(BasePermission):

    def has_permission(self, request, view):
        return isinstance(request.user, Shop)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsShopOwner(IsAuthenticatedShop):

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'shop') and request.user != obj.shop:
            return False
        return super(IsShopOwner, self).has_object_permission(request, view, obj)


class IsShopOwnerOrReadOnly(IsShopOwner):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return super(IsShopOwnerOrReadOnly, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return super(IsShopOwnerOrReadOnly, self).has_object_permission(request, view, obj)


class HasShop(BasePermission):

    def has_permission(self, request, view):
        if request.shop:
            if isinstance(request.user, Shop) and request.shop != request.user:
                raise exceptions.ParseError('shop and user of request are not matched!')
        else:
            if isinstance(request.user, Shop):
                request.shop = request.user
            if isinstance(request.user, Customer):
                request.shop = request.user.shop
        return bool(request.shop)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
