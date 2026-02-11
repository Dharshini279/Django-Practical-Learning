from django.shortcuts import render, redirect, get_object_or_404
from apps.products.forms.product_forms import ProductForm, VariantForm
from apps.products.services.product_service import create_product_with_variant
from apps.products.selectors.product_selectors import get_all_products
from apps.products.models import Product


def product_list(request):
    products = get_all_products()
    return render(request, "products/product_list.html", {"products": products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        variant_form = VariantForm(request.POST)

        if form.is_valid() and variant_form.is_valid():
            create_product_with_variant(
                form.cleaned_data,
                variant_form.cleaned_data
            )
            return redirect("products:list")

    else:
        form = ProductForm()
        variant_form = VariantForm()

    return render(
        request,
        "products/product_create.html",
        {"form": form, "variant_form": variant_form},
    )
