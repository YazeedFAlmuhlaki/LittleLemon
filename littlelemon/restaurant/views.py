from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import MenuSerializer,BookingSerializer
from .models import Menu,Booking

def index(request):
    return render(request, 'index.html')

class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]         
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny] 

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]          
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]
    
class BookingListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetailView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
