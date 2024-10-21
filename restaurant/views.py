from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import MenuItem, booking
from .serializers import MenuItemItemSerializer, BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class MenuItemsView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemItemSerializer

class BookingViewSet(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = bookingSerializer

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})