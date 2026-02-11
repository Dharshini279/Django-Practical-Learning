from django.shortcuts import render
from apps.products.models import Category
from apps.products.forms.product_forms import CategoryForm
from django.shortcuts import redirect

def category_list(request):
    categories = Category.objects.all()
    return render(request, "products/category_list.html", {"categories": categories})


def category_create(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:category_list")

    return render(request, "products/category_create.html", {"form": form})