from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from django.contrib.auth.models import User



class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')

class UserDetailSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ('id','username','first_name','last_name','email')

class UserListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_user_detail_url',
        lookup_field='id'
    )
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','url')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')