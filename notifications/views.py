from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .serializers import ProductInventorySerializer

class InventoryAPIView(APIView):
    def get(self, request, format=None):
        serializer = ProductInventorySerializer(settings.INVENTORY_SETTINGS, many=True)
        return Response(serializer.data)
