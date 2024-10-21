from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuItem, booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = "__all__"