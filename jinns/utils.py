import random

import requests
from rest_framework.exceptions import APIException

from shops.models import Shop

HTTP_494_HEYSHOP_API_ERROR = 494


class HeyshopApiError(APIException):
    status_code = HTTP_494_HEYSHOP_API_ERROR
    default_detail = 'heyshop_api_error'
    default_code = 'heyshop_api_error'


def make_random_slug(n=6, case='lower'):
    start = int('0xA%s' % ('0' * (n - 1)), 16)
    end = int('0x%s' % ('F' * n), 16)
    num = random.randint(start, end)
    code = hex(num)[2:]
    return code.lower() if case == 'lower' else code.upper()


def shop_api_request(url, shop=None, method='get', **kwargs):

    token = shop.access_token

    assert token and shop, (url, token, shop)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token,
    }

    if kwargs.pop('bulk', False):
        headers['X-BULK-OPERATION'] = '1'

    if 'http' not in url:
        url = 'https://%s.heidianer.com%s' % (shop.name, url)

    r = requests.request(method, url, headers=headers, **kwargs)

    if r.status_code >= 400:
        e = {'detail': r.text, 'url': url, 'method': method}
        e.update(kwargs)
        raise HeyshopApiError(e)

    try:
        return r.json()
    except:
        return r.text


def heyshop_plain_api_request(url, method='get', **kwargs):

    # 单纯的向 heyshop.heidianer.com 发请求，不带任何 header

    if 'http' not in url:
        url = 'https://heyshop.heidianer.com%s' %  url

    r = requests.request(method, url, **kwargs)

    if r.status_code >= 400:
        e = {'detail': r.text, 'url': url, 'method': method}
        e.update(kwargs)
        raise HeyshopApiError(e)

    try:
        return r.json()
    except:
        return r.text


def get_shop_name_by_domain(domain):
    url = 'https://heidianapi.com/api/shops/shop_front/'
    r = requests.get(url, headers={'x-shop-domain': domain}).json()
    shop_name = r['shop']['name']
    return shop_name


def get_shop_by_domain(domain):
    shop_name = get_shop_name_by_domain(domain)
    shop = Shop.objects.filter(name=shop_name).first()
    return shop
