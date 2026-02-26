from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import InventoryItem
from .serializers import InventoryItemSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users see only their own items
        return InventoryItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as owner
        serializer.save(user=self.request.user)
