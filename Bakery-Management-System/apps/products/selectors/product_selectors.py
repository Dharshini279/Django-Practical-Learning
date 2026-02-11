from apps.products.models import Product


def get_all_products():
    return Product.objects.select_related("category").prefetch_related("variants")


def get_active_products():
    return Product.objects.filter(is_active=True)
