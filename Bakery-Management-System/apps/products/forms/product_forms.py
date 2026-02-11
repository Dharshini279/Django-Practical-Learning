from django import forms
from apps.products.models import Product, ProductVariant, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "description", "is_active"]


class VariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ["size", "price", "sku", "is_available"]
