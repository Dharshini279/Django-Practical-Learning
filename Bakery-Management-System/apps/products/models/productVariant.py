from django.db import models
from .product import Product

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} - {self.size}"
