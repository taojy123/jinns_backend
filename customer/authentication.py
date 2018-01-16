
from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from customer.models import Customer
from shop.models import Shop


class CustomerTokenAuthentication(TokenAuthentication):
    keyword = 'customertoken'
    model = Customer

    def authenticate(self, request):
        token = request.data.get(self.keyword)
        if token:
            return self.authenticate_credentials(token)
        return super(CustomerTokenAuthentication, self).authenticate(request)

    def authenticate_credentials(self, token):
        model = self.get_model()
        try:
            customer = model.objects.get(token=token)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))
        return customer, customer
