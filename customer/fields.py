from customer.models import Customer


class CurrentCustomerDefault(object):

    customer = None

    def set_context(self, serializer_field):
        self.customer = serializer_field.context['request'].user
        assert isinstance(self.customer, Customer)

    def __call__(self):
        return self.customer

    def __repr__(self):
        return '%s()' % self.__class__.__name__
