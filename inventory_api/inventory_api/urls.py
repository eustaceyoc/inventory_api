from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

def api_root(request):
    return JsonResponse({
        "message": "Inventory Management API is running",
        "endpoints": {
            "inventory": "/api/inventory/",
            "logs": "/api/logs/",
            "token": "/api/token/",
        }
    })

schema_view = get_schema_view(
    openapi.Info(
        title="Inventory API",
        default_version='v1',
        description="API documentation for Inventory Management system",
        contact=openapi.Contact(email="your@email.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)

swagger_view = csrf_exempt(schema_view.with_ui('swagger', cache_timeout=0))
redoc_view = csrf_exempt(schema_view.with_ui('redoc', cache_timeout=0))

urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/inventory/', include('inventory.urls')),
    path('api/logs/', include('inventory_logs.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger/', swagger_view, name='schema-swagger-ui'),
    path('redoc/', redoc_view, name='schema-redoc'),
]