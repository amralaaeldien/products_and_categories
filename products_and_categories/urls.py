from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products_and_categories import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
	path("products/<str:product_code>", views.ProductDetail.as_view(), name="product-detail"),
	path("categories/<str:name>", views.CategoryDetail.as_view(), name="category-detail"),

]