from django.urls import path

from .views import ProductListView, InventoryAPIView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('inventory/<int:product_id>/', InventoryAPIView.as_view(), name='inventory-metrics'),
]
