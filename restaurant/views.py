from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import menu, booking
from .serializers import MenuItemSerializer, BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class MenuItemsView(generics.ListCreateAPIView):
    quryset = menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(generics.ListCreateAPIView):
    serializer_class = bookingSerializer
