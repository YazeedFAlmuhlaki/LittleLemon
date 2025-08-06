from django.urls import path
from .views import (
    MenuItemsView, SingleMenuItemView,
    BookingListCreateView, BookingDetailView
)

urlpatterns = [
    path('menu/',      MenuItemsView.as_view(),      name='menu-list'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
    path('booking/',      BookingListCreateView.as_view(),      name='booking-list'),
    path('booking/<int:pk>/', BookingDetailView.as_view(),      name='booking-detail'),
]
