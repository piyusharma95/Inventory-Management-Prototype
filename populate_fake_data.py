import os
import django
import random
from faker import Faker
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_management.settings')
django.setup()

from notifications.models import Product, Sale  # Import after setting up Django

fake = Faker()

def create_products(n):
    for _ in range(n):
        product = Product.objects.create(
            name=fake.word().capitalize(),
            current_stock=random.randint(50, 200),
            lead_time=random.randint(1, 20),
            alert_threshold=random.randint(10, 50)
        )
        create_sales(product, random.randint(30, 100))

def create_sales(product, count):
    for _ in range(count):
        Sale.objects.create(
            product=product,
            quantity=random.randint(1, 10),
            sale_date=fake.date_between(start_date='-90d', end_date='today')
        )

if __name__ == '__main__':
    print("Creating products and sales...")
    create_products(10)  # Create 10 products with associated sales
    print("Data generation complete!")
