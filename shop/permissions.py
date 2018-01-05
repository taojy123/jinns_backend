
from rest_framework.permissions import BasePermission, SAFE_METHODS

from shop.models import Shop


class IsAuthenticatedShop(BasePermission):

    def has_permission(self, request, view):
        return request.user and isinstance(request.user, Shop)

    def has_object_permission(self, request, view, obj):
        return request.user and isinstance(request.user, Shop)


class IsShopOwner(IsAuthenticatedShop):

    def has_object_permission(self, request, view, obj):
        return hasattr(obj, 'shop') and request.user == obj.shop


class IsShopOwnerOrReadOnly(IsShopOwner):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return super(IsShopOwnerOrReadOnly, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return super(IsShopOwnerOrReadOnly, self).has_object_permission(request, view, obj)


class HasShopDomain(BasePermission):

    def has_permission(self, request, view):
        return bool(request.shop_domain)

    def has_object_permission(self, request, view, obj):
        return bool(request.shop_domain)

