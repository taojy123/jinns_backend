
from rest_framework import generics, response, exceptions, viewsets
from rest_framework.decorators import list_route

from customer.models import Customer, CouponCode
from customer.permissions import IsCustomerOwner
from customer.serializers import CustomerSerializer, CouponCodeSerializer
from order.models import Order
from order.serializers import OrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [IsCustomerOwner]
    pagination_class = None

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
    permission_classes = [IsCustomerOwner]
    pagination_class = None

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

    @list_route(methods=['post'], permission_classes=[])
    def checkout(self, request, *args, **kwargs):
        customer = request.user

        tips = 'room 格式为 [{"id": 5, "count": 2}, ...]'
        rooms = request.data.get('rooms')
        if not isinstance(rooms, list):
            raise exceptions.ParseError(tips)

        rs = []
        for room in rooms:
            room_id = room.get('id')
            count = room.get('count')
            if not isinstance(room_id, int):
                raise exceptions.ParseError(tips)
            if room_id <= 0:
                raise exceptions.ParseError(tips)
            if not isinstance(count, int):
                raise exceptions.ParseError(tips)
            if count <= 0:
                raise exceptions.ParseError(tips)
            rs.append((room_id, count))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        order = serializer.instance

        order.category = 'room'
        if isinstance(customer, Customer):
            order.customer = customer

        for room_id, count in rs:
            order.orderroom_set.create(room_id=room_id, quantity=count)

        order.calculate_total_price()
        order.save()

        return response.Response(self.get_serializer(order).data)
