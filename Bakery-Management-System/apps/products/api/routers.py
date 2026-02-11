from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="api-products")
router.register("categories", CategoryViewSet, basename="api-categories")
