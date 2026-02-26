from django.db import models
from django.conf import settings
from shop_products.models import Product
# from products.models import Product   # <-- comment this temporarily

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)  # comment temporarily too
    quantity = models.PositiveIntegerField(default=1)