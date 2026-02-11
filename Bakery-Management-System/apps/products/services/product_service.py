from apps.products.models import Product, ProductVariant


def create_product_with_variant(product_data, variant_data):
    product = Product.objects.create(**product_data)

    ProductVariant.objects.create(
        product=product,
        **variant_data
    )

    return product


def get_product_with_variants(product_id):
    return Product.objects.prefetch_related("variants").get(id=product_id)
