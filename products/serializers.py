


from django.contrib.auth import get_user_model

from rest_framework import serializers
from accounts.models import UserAccount
from products.models import Wishlist

from products.models import Product
from products.models import Category
from products.models import OrderItem
from products.models import Order
from products.models import ShippingAddress
from accounts.serializers import UserCreateSerializer



class ProductSerializer(serializers.ModelSerializer):
    category=serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='id')
    image = serializers.ImageField(max_length=None,allow_empty_file=False, use_url=True, allow_null=False,required=False)


    class Meta:
    
        model = Product
        fields='__all__'
        
class WishlistSerializer(serializers.ModelSerializer):
    user=serializers.SlugRelatedField(queryset=UserAccount.objects.all(), slug_field='id')
    product=serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='id')


    class Meta:
    
        model = Wishlist
        fields='__all__'
        
class CategorySerializer(serializers.ModelSerializer):


    class Meta:
    
        model = Category
        fields='__all__'
        
class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    User = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderItems(self,obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items,many=True)
        return serializer.data

    def get_shippingAddress(self,obj):
        try:
            address = ShippingAddressSerializer(obj.shippingaddress,many=False).data
        except:
            address = False
        return address

    def get_User(self,obj):
        items = obj.user
        serializer = UserCreateSerializer(items,many=False)
        return serializer.data



