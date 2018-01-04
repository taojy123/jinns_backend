

class Middleware(object):

    def process_request(self, request):
        _ = request.body
        """
        Don't delete above line! calling request.body will call request.read()
        This is for the purpose of displaying the request body in error report mail.
        """

        request.shop_domain = request.GET.get('shop')

        # x-shop-domain
        if not request.shop_domain and 'HTTP_X_SHOP_DOMAIN' in request.META:
            request.shop_domain = request.META['HTTP_X_SHOP_DOMAIN']


