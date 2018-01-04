import requests
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from rest_framework import generics, response, exceptions

from jinns.utils import get_shop_name_by_domain
from shops.models import Shop, ShopToken
from shops.serializers import ShopTokenSerializer


def generate_token_by_code(code, shop_domain):

    shop_name = get_shop_name_by_domain(shop_domain)

    url = 'https://%s/api/oauth/token/' % shop_domain

    params = {
        'code': code,
        'redirect_uri': settings.DEFAULT_REDIRECT_URI,
        'grant_type': 'authorization_code',
    }

    auth = (settings.CLIENT_ID, settings.CLIENT_SECRET)

    try:
        r = requests.post(url, params=params, auth=auth)
        data = r.json()
    except Exception as e:
        raise exceptions.ParseError(str(e))

    if 'access_token' not in data:
        raise exceptions.ParseError(data)

    shop, created = Shop.objects.get_or_create(name=shop_name)
    shop.shop_id = data['shop_id']
    shop.save()

    token = ShopToken()
    token.shop = shop
    token.access_token = data['access_token']
    token.refresh_token = data['refresh_token']
    token.scope = data['scope']
    token.expires_in = data['expires_in']
    token.save()

    if created:
        shop.initialize()

    return token


def oauth_jump(request):

    shop_domain = request.GET.get('shop', '')
    scope = request.GET.get('scope', 'read write')
    redirect_uri = request.GET.get('redirect_uri', settings.DEFAULT_REDIRECT_URI)

    shop_name = get_shop_name_by_domain(shop_domain)

    jump_url = 'https://%s/api/oauth/authorize/?scope=%s&state=%s&redirect_uri=%s&response_type=code&client_id=%s' % (
        shop_domain, scope, shop_name, redirect_uri, settings.CLIENT_ID
    )

    return HttpResponseRedirect(jump_url)


class GenerateTokenView(generics.GenericAPIView):
    serializer_class = ShopTokenSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        code = request.data.get('code')
        shop_domain = request.data.get('shop')

        token = generate_token_by_code(code, shop_domain)

        return response.Response(self.get_serializer(token).data)


