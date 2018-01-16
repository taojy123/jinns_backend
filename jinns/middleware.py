from rest_framework import exceptions

from shop.models import Shop


class Middleware(object):

    def process_request(self, request):
        _ = request.body
        """
        Don't delete above line! calling request.body will call request.read()
        This is for the purpose of displaying the request body in error report mail.
        """

        shop_id = request.GET.get('shop_id')

        # x-shop-id
        if not shop_id and 'HTTP_X_SHOP_ID' in request.META:
            shop_id = request.META['HTTP_X_SHOP_ID']

        shop = Shop.objects.filter(id=shop_id).first()

        request.shop = shop




