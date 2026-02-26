from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class InventoryLogList(APIView):
    def get(self, request):
        return Response({"message": "Inventory logs endpoint - coming soon"})

class InventoryLogDetail(APIView):
    def get(self, request, pk):
        return Response({"message": f"Inventory log detail {pk} - coming soon"})
