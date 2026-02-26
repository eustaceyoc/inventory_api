from django.urls import path
from . import views

urlpatterns = [
    path('', views.InventoryLogList.as_view(), name='logs-list'),
    path('<int:pk>/', views.InventoryLogDetail.as_view(), name='logs-detail'),
]
