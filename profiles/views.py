

from django.shortcuts import render

#from rest_framework.response import Response
#from rest_framework.decorators import api_view

from .serializers import ProfileSerializer
from .models import UserProfile
from rest_framework import viewsets


class ProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer