from django.shortcuts import render

from .serializers import CategorySerializer, WishlistSerializer,ProductSerializer,OrderSerializer
from accounts.serializers import UserCreateSerializer
from .models import Category,Product,Order,OrderItem,ShippingAddress,Wishlist
# Rest Framework Import

from rest_framework import viewsets
from django.contrib.auth import get_user_model

from datetime import datetime

from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.serializers import Serializer




class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class WishlistView(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer




class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

user = get_user_model()

@api_view(['POST'])
def addOrderItems(request):
    user = request.user
    data = request.data
    print(data)
    orderItems = data['orderItems']

    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order Items', "status": status.HTTP_400_BAD_REQUEST})
    else:
        # (1) Create Order
        order = Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            shippingPrice=data['shippingPrice'],
            totalPrice=data['totalPrice'],
        )

        # (2) Create Shipping Address

        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            postalCode=data['shippingAddress']['postalCode'],
            country=data['shippingAddress']['country'],
        )

        # (3) Create order items

        for i in orderItems:
            product = Product.objects.get(id=i['product'])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.title,
                qty=i['qty'],
                price=i['price'],
                image=product.image,
            )

            # (4) Update Stock

            product.countInStock -= item.qty
            product.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)


@api_view(['GET'])
def getMyOrders(request):
     
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
    # user =request.user
    # # orders = Order.objects.filter(user=user)
    # orders = user.order_set.all()
    # serializer = OrderSerializer(orders, many=True)
    # return Response(serializer.data)


@api_view(['GET'])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

User = get_user_model()

@api_view(['GET'])
def getOrderById(request, pk):



    user = request.user

    order = Order.objects.get(id=pk)
    # if user.is_staff or order.user == User:
    serializer = OrderSerializer(order, many=False)
    
    return Response(serializer.data)
    

@api_view(['PUT'])
def updateOrderToPaid(request, pk):
    order = Order.objects.get(id=pk)
    order.isPaid = True
    order.paidAt = datetime.now()
    order.save()
    return Response('Order was paid')


@api_view(['PUT'])
def updateOrderToDelivered(request, pk):
    order = Order.objects.get(id=pk)
    order.isDeliver = True
    order.deliveredAt = datetime.now()
    order.save()
    return Response('Order was Delivered')

