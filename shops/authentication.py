
from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from shops.models import ShopToken


class ShopTokenAuthentication(TokenAuthentication):
    keyword = 'shoptoken'
    model = ShopToken

    def authenticate_credentials(self, access_token):
        model = self.get_model()
        try:
            token = model.objects.get(access_token=access_token)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        return token.user, token
