from django.shortcuts import render
from apps.products.models import Category


def category_list(request):
    categories = Category.objects.all()
    return render(request, "products/category_list.html", {"categories": categories})
