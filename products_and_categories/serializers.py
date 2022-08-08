from rest_framework import serializers
from products_and_categories.models import Product, Category
from django.db import models

class CategorySerializer(serializers.ModelSerializer):
	sub_categories = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
		queryset=Category.objects.all(),
		allow_null=True,
		required = False
     )
	link = serializers.HyperlinkedIdentityField(view_name="category-detail", lookup_field="name")

	class Meta:
		model = Category
		fields = ("name","link", 'products', 'sub_categories')
		
	
class ProductSerializer(serializers.ModelSerializer):
	link = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="product_code")
	categories = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
		queryset=Category.objects.all(),
		allow_null=True,
		required = False
     )
	
	class Meta:
		model = Product
		fields = ( "product_code", "name", "link", "quantity", "price", 'categories')

	def update(self, instance, validated_data):

		instance.product_code = validated_data.get('product_code', instance.product_code)
		instance.name = validated_data.get('name', instance.name)
		instance.quantity = validated_data.get('quantity', instance.quantity)
		instance.price = validated_data.get('price', instance.price)
		instance.categories.set(validated_data.get('categories', instance.categories))
		
		instance.save()
		return instance

	def create(self, validated_data):		
		if "categories" in validated_data:
			category_data = validated_data.pop('categories')
			product = Product.objects.create(**validated_data)
			for category in category_data:
				product.categories.add(category)
			return product
		product = Product.objects.create(**validated_data)
		return product


