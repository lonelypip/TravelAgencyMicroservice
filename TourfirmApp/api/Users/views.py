from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, JsonResponse 
from django.contrib.auth.models import User


from .serializers import (
    UserListSerializer,    
    UserDetailSerializer,
    UserUpdateSerializer,
    UserCreateSerializer
)
from .permissions import IsOwnerOrReadOnly


from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import (
   IsAuthenticated,
)
from rest_framework.generics import (
   ListAPIView, 
   RetrieveAPIView, 
   UpdateAPIView, 
   DestroyAPIView, 
   CreateAPIView,
   RetrieveUpdateAPIView
)

from rest_framework.authentication import TokenAuthentication

class UserListAPIView(ListAPIView): 
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    #def get_queryset()


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    lookup_field = 'id'


class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'id'
   


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    
