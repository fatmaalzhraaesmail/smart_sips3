from rest_framework import serializers
from profiles.serializers import ProfileSerializer
from products.models import Order
from profiles.models import UserProfile
from djoser.serializers import UserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from django.http import JsonResponse
from django.core.serializers import serialize
import json

from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    # profile = ProfileSerializer(read_only=True)
    profile = ProfileSerializer()


    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password','is_staff','profile',)
        read_only_fields = ( 'profile',)



# class UpdateUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = '__all__'

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data['first_name']
#         instance.last_name = validated_data['last_name']
#         instance.email = validated_data['email']
#         instance.username = validated_data['username']
#         instance.facebook_url = validated_data['facebook_url']
#         instance.instagram_url = validated_data['instagram_url']
#         instance.twitter_url = validated_data['twitter_url']
#         instance.job = validated_data['job']
#         instance.birth_date = validated_data['birth_date']
#         instance.profile_pic = validated_data['profile_pic']
#         instance.phone = validated_data['phone']

#         instance.save()

#         return instance 
    
   
# class PasswordSerializer(serializers.Serializer):
        model = User

   
        current_password = serializers.CharField(required=True)
        new_password = serializers.CharField(required=True)
        re_new_password = serializers.CharField(required=True)
    
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password','profile')
        read_only_fields = ('username','email','password', 'first_name', 'last_name' ,'profile')



