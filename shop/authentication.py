
from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from shop.models import Shop


class ShopTokenAuthentication(TokenAuthentication):
    keyword = 'shoptoken'
    model = Shop

    def authenticate_credentials(self, token):
        model = self.get_model()
        try:
            shop = model.objects.get(token=token)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        return shop, shop
