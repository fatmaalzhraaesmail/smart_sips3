# from rest_framework import serializers
# from .models import UserProfile

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'


from django.contrib.auth import get_user_model

from rest_framework import serializers
from accounts.models import UserAccount

from profiles.models import UserProfile

# User = get_user_model()


# class UserProfileSerializer(serializers.ModelSerializer):
#     """Serializer To Show User Profile In User Dashboard"""

#     website = serializers.URLField(
#         source='profile.website', allow_blank=True, allow_null=True)
#     bio = serializers.CharField(
#         source='profile.bio', allow_blank=True, allow_null=True)
#     country = serializers.CharField(
#         source='profile.country', allow_blank=True, allow_null=True)
#     facebook_url = serializers.URLField(
#         source='profile.facebook_url', allow_blank=True, allow_null=True)
#     twitter_handler = serializers.CharField(
#         source='profile.twitter_handler', allow_blank=True, allow_null=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name',
#                   'website', 'bio', 'country', 'facebook_url', 'twitter_handler']

#     def update(self, instance, validated_data):
#         """Overwriting The Default update Method For This Serializer
#         To Update User And UserProfile At A Single Endpoint"""

#         profile_data = validated_data.pop('profile', None)
#         self.update_or_create_profile(instance, profile_data)
#         return super(UserProfileSerializer, self).update(instance, validated_data)

#     def update_or_create_profile(self, user, profile_data):
#         """This always creates a Profile if the User is missing one"""

#         UserProfile.objects.update_or_create(user=user, defaults=profile_data)        
# from django.contrib.auth import get_user_model

# from rest_framework import serializers
# from django_countries.fields import CountryField


# from profiles.models import UserProfile

# User = get_user_model()


# class UserProfileSerializer(serializers.ModelSerializer):
#     """Serializer To Show User Profile In User Dashboard"""

#     job = serializers.CharField(
#         source='profile.job', allow_blank=True, allow_null=True)
#     birth_date = serializers.CharField(
#         source='profile.birth_date', allow_blank=True, allow_null=True)
#     country = serializers.CountryField(
#         source='profile.country', allow_blank=True, allow_null=True)
#     facebook_url = serializers.CharField(
#         source='profile.facebook_url', allow_blank=True, allow_null=True)
#     twitter_url = serializers.CharField(
#         source='profile.twitter_url', allow_blank=True, allow_null=True)
#     instagram_url = serializers.CharField(
#         source='profile.instagram_url', allow_blank=True, allow_null=True)
#     profile_pic = serializers.ImageField( source='profile.profile_pic', allow_blank=True, allow_null=True, upload_to="accounts/images/")


#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name',
#                   'job', 'birth_date','instagram_url', 'country', 'facebook_url', 'twitter_url','profile_pic']

#     def update(self, instance, validated_data):
#         """Overwriting The Default update Method For This Serializer
#         To Update User And UserProfile At A Single Endpoint"""

#         profile_data = validated_data.pop('profile', None)
#         self.update_or_create_profile(instance, profile_data)
#         return super(UserProfileSerializer, self).update(instance, validated_data)

#     def update_or_create_profile(self, user, profile_data):
#         """This always creates a Profile if the User is missing one"""

#         UserProfile.objects.update_or_create(user=user, defaults=profile_data)
# class SerializableCountryField(serializers.ChoiceField):
#     def to_representation(self, value):
#         if value in ('', None):
#             return ''  # instead of `value` as Country(u'') is not serializable
#         return super(SerializableCountryField, self).to_representation(value)
from django_countries.serializer_fields import CountryField

class ProfileSerializer(serializers.ModelSerializer):
    # user = UserCreateSerializer(read_only=True)
    user=serializers.SlugRelatedField(queryset=UserAccount.objects.all(), slug_field='id')
    country = CountryField()
    profile_pic = serializers.ImageField(max_length=None,allow_empty_file=False, use_url=True, allow_null=False,required=False)


   

    
    class Meta:
    
        model = UserProfile
        fields='__all__'
        
        # fields = ('first_name', 'last_name','country', 'facebook_url','twitter_url','profile_pic','job','instagram_url','birth_date','user')

