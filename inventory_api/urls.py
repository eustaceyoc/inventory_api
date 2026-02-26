"""
URL configuration for inventory_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Inventory Management API is running",
        "endpoints": {
            "inventory": "/api/inventory/",
            "logs": "/api/logs/",
        }
    })

urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
    path('api/', include('inventory_logs.urls')),
    path('', views.InventoryItemList.as_view(), name='inventory-list'),
    path('<int:pk>/', views.InventoryItemDetail.as_view(), name='inventory-detail'),
]
