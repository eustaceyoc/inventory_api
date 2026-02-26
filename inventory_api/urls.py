from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # if you create user endpoints
    path('api/inventory/', include('inventory.urls')),
]
