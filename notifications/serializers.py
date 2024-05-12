from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class InventoryMetricsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    total_sales_last_90_days = serializers.IntegerField()
    current_stock = serializers.IntegerField()
    lead_time = serializers.IntegerField()
    alert_threshold = serializers.IntegerField()
    days_until_out_of_stock = serializers.SerializerMethodField()
    should_alert_be_sent = serializers.SerializerMethodField()
    days_left_before_alert = serializers.SerializerMethodField()

    def get_days_until_out_of_stock(self, obj):
        daily_rate = obj['total_sales_last_90_days'] / 90
        return obj['current_stock'] / daily_rate if daily_rate else float('inf')

    def get_should_alert_be_sent(self, obj):
        days_until_empty = self.get_days_left_before_alert(obj)
        return days_until_empty == 0

    def get_days_left_before_alert(self, obj):
        daily_rate = obj['total_sales_last_90_days'] / 90
        if daily_rate == 0:
            return float('inf')  # Prevent division by zero
        days_until_alert = (obj['current_stock'] - obj['alert_threshold']) / daily_rate
        return max(0, days_until_alert - obj['lead_time'])
