from rest_framework import serializers
from .models import InventoryItem

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = [
            'id',
            'user',
            'name',
            'description',
            'quantity',
            'price',
            'category',
            'date_added',
            'last_updated',
        ]
        read_only_fields = ['id', 'user', 'date_added', 'last_updated']
