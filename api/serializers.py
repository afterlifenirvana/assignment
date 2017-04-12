from rest_framework import serializers
from models import *
from django.contrib.auth.models import User, Group
from rest_framework_mongoengine.serializers import DocumentSerializer 



class RestaurantSerializer(DocumentSerializer):
    class Meta:
        model = Restaurants
        fields = '__all__'


        
# class RestaurantSerializer(serializers.ModelSerializer):
#     class Meta:
#     	model = Restaurants 
#     	fields = ('address','borough','cuisine','grades','name','restaurant_id')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')