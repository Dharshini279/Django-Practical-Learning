from django.urls import path
from apps.products.views import product_view, category_view

app_name = "products"

urlpatterns = [
    path("", product_view.product_list, name="list"),
    path("create/", product_view.product_create, name="create"),
    path("<int:pk>/", product_view.product_detail, name="detail"),
    path("categories/", category_view.category_list, name="categories"),
    path("categories/create/", category_view.category_create, name="category_create")
]
