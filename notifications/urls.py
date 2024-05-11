from django.urls import path
from .views import InventoryAPIView

urlpatterns = [
    path('inventory/', InventoryAPIView.as_view(), name='inventory-list'),
]
