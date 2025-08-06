# littlelemon/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # DRF’s built-in token view
    path('api-token-auth/', obtain_auth_token),

    # All Restaurant app routes under /restaurant/
    path('restaurant/', include('restaurant.urls')),
]
