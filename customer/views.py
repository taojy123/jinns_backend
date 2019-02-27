from django.db.models import Q
from rest_framework import generics, response, exceptions, viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.generics import get_object_or_404
from django_filters import rest_framework as filters, STRICTNESS

from customer.models import Customer, CouponCode
from customer.permissions import IsCustomerOwner, IsCustomerOwnerOrReadOnly
from customer.serializers import CustomerSerializer, CouponCodeSerializer
from order.models import Order
from order.serializers import OrderSerializer
from order.views import OrderFilter


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsCustomerOwner]
    pagination_class = None

    def get_object(self):
        return self.get_queryset().get()

    def get_queryset(self):
        return Customer.objects.filter(id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CouponCodeViewSet(viewsets.ModelViewSet):
    serializer_class = CouponCodeSerializer
    permission_classes = [IsCustomerOwner]
    pagination_class = None

    def get_queryset(self):
        return CouponCode.objects.filter(customer=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsCustomerOwnerOrReadOnly]
    pagination_class = None
    filter_class = OrderFilter
    lookup_field = 'order_number'

    def get_object(self):
        obj = get_object_or_404(Order, order_number=self.kwargs['order_number'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        if not isinstance(self.request.user, Customer):
            raise exceptions.NotAuthenticated()
        return Order.objects.filter(customer=self.request.user).order_by('-id')

    @list_route(methods=['post'], permission_classes=[])
    def checkout(self, request, *args, **kwargs):
        customer = request.user

        # room, products : [{"id": 5, "count": 2}, ...]

        rooms = request.data.get('rooms') or []
        products = request.data.get('products') or []

        rs = []
        for room in rooms:
            room_id = room.get('id')
            count = room.get('count')
            rs.append((room_id, count))

        ps = []
        for product in products:
            product_id = product.get('id')
            count = product.get('count')
            ps.append((product_id, count))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        order = serializer.instance

        for room_id, count in rs:
            order.orderroom_set.create(room_id=room_id, quantity=count)

        for product_id, count in ps:
            order.orderproduct_set.create(product_id=product_id, quantity=count)

        if isinstance(customer, Customer):
            order.customer = customer

        order.calculate_total_price()
        order.save()

        return response.Response(self.get_serializer(order).data)

    @detail_route(methods=['get'])
    def coupon_codes(self, request, *args, **kwargs):
        customer = request.user
        data = CouponCodeSerializer(customer.couponcode_set.all(), many=True).data
        for item in data:
            item['key'] = item['id']
            item['value'] = '%s [¥%s]' % (item['coupon']['name'], item['coupon']['price'])
        return response.Response(data)

    @detail_route(methods=['post'])
    def pay(self, request, *args, **kwargs):
        order = self.get_object()
        customer = request.user
        assert order.customer == customer, (order.id, customer.id)
        coupon_code_id = request.data.get('coupon_code_id')
        channel = request.data.get('channel')
        if coupon_code_id:
            coupon_code = CouponCode.objects.get(id=coupon_code_id)
            order.use_coupon = coupon_code
        if channel == 'balance':
            use_balance = min(customer.balance, order.unpaid_price)
            customer.balancehistory_set.create(amount=-use_balance, reason='#%s订单抵扣' % order.order_number)
            order.use_balance = use_balance
        if channel == 'point':
            use_point_price = min(customer.point / 100, order.unpaid_price)
            customer.pointhistory_set.create(amount=-use_point_price * 100, reason='#%s订单抵扣' % order.order_number)
            order.use_point = use_point_price

        order.save()

        if order.unpaid_price == 0:
            order.payment_success()

        order.refresh_from_db()
        
        return response.Response(self.get_serializer(order).data)



class GetCustomerTokenView(generics.GenericAPIView):
    serializer_class = CustomerSerializer
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        openid = request.query_params.get('openid')
        customer = get_object_or_404(Customer, openid=openid)
        return response.Response({'token': customer.token})
