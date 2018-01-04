
from shops.models import Shop


class CurrentShopDefault(object):

    shop = None

    def set_context(self, serializer_field):
        self.shop = serializer_field.context['request'].user
        assert isinstance(self.shop, Shop)

    def __call__(self):
        return self.shop

    def __repr__(self):
        return '%s()' % self.__class__.__name__

