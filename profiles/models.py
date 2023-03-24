# from django.db import models
# # from django.contrib.auth.models import User
from django_countries.fields import CountryField



from django.db import models
from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver

User = get_user_model()

# class ImageField(models.ImageField):
#     def value_to_string(self, obj): # obj is Model instance, in this case, obj is 'Class'
#         return obj.fig.url
    
class UserProfile(models.Model):
    """Model For Extending Default Django User Model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    first_name = models.CharField(max_length=255,null=True,blank=True,)
    last_name = models.CharField(max_length=255,null=True,blank=True,)
    job = models.CharField(max_length=255,null=True,blank=True,)
    phone = models.CharField(max_length=255,null=True,blank=True,)
    facebook_url =models.CharField(max_length=255,null=True,blank=True,)
    twitter_url =models.CharField(max_length=255,null=True,blank=True,)
    instagram_url =models.CharField(max_length=255,null=True,blank=True,)
    birth_date =models.DateField(null=True,blank=True,)
    country = CountryField(null=True,blank=True,)
    # country = models.CharField(max_length=255,null=True,blank=True,)

    profile_pic = models.ImageField(null=True, blank=True, upload_to="accounts/images/")
   

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username
    # @property
    # def profile_pic(self):
    #     return self.profile_pic


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, *args, **kwargs):

#     if created:
#         user_profile = UserProfile(user=instance)
#         user_profile.save()