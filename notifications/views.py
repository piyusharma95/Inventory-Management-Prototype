from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer, InventoryMetricsSerializer



class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class InventoryAPIView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            metrics = {
                'total_sales_last_90_days': product.sales_last_90_days(),
                'current_stock': product.current_stock,
                'lead_time': product.lead_time,
                'alert_threshold': product.alert_threshold,
            }
            serializer = InventoryMetricsSerializer(metrics)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)