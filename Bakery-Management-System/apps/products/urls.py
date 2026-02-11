from django.urls import path
from apps.products.views import product_views, category_views

app_name = "products"

urlpatterns = [
    path("", product_views.product_list, name="list"),
    path("create/", product_views.product_create, name="create"),
    path("<int:pk>/", product_views.product_detail, name="detail"),
    path("categories/", category_views.category_list, name="categories"),
]
