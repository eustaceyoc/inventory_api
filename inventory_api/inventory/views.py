from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class InventoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'quantity', 'price', 'date_added']

    def get_queryset(self):
        queryset = InventoryItem.objects.filter(user=self.request.user)

        low_stock_threshold = self.request.query_params.get('low_stock', None)
        if low_stock_threshold is not None:
            try:
                threshold = int(low_stock_threshold)
                queryset = queryset.filter(quantity__lte=threshold)
            except ValueError:
                pass

        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        if min_price is not None:
            try:
                queryset = queryset.filter(price__gte=float(min_price))
            except ValueError:
                pass
        if max_price is not None:
            try:
                queryset = queryset.filter(price__lte=float(max_price))
            except ValueError:
                pass

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
