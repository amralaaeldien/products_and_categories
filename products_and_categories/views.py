from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.
from rest_framework import viewsets
from products_and_categories.models import Product, Category
from products_and_categories.serializers import ProductSerializer, CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryDetail(RetrieveUpdateDestroyAPIView):
	lookup_field = "name"
	lookup_url_kwarg = "name"
	queryset= Category.objects.all()
	serializer_class = CategorySerializer
	

class ProductDetail(RetrieveUpdateDestroyAPIView):
	lookup_field = "product_code"
	lookup_url_kwarg = "product_code"
	queryset= Product.objects.all()
	serializer_class = ProductSerializer
