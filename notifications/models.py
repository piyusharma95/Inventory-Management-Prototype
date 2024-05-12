from datetime import timedelta

from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=255)
    current_stock = models.IntegerField(default=0)
    lead_time = models.IntegerField(default=0)  # in days
    alert_threshold = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def sales_last_90_days(self):
        ninety_days_ago = timezone.now().date() - timedelta(days=90)
        return self.sales.filter(sale_date__gte=ninety_days_ago).aggregate(total=models.Sum('quantity'))['total'] or 0


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    quantity = models.IntegerField(default=0)
    sale_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.quantity} units of {self.product.name} sold on {self.sale_date}"
