from rest_framework import serializers
from products_and_categories.models import Product, Category
from django.db import models

class CategorySerializer(serializers.ModelSerializer):
	def to_representation(self, obj):
		if 'categories' not in self.fields:
			self.fields['categories'] = CategorySerializer(obj, many=True)      
		return super(CategorySerializer, self).to_representation(obj)

	class Meta:
		model = Category
		fields = ('id', "name", 'products', 'categories')
	
class ProductSerializer(serializers.ModelSerializer):
	categories = CategorySerializer(many=True, required=False)

	class Meta:
		model = Product
		fields = ('id', "product_code", "name", "quantity", "price", 'categories')

	def update(self, instance, validated_data):
		if 'categories' in validated_data:
			category_data = validated_data.pop('categories')

		instance.product_code = validated_data.get('product_code', instance.product_code)
		instance.name = validated_data.get('name', instance.name)
		instance.quantity = validated_data.get('quantity', instance.quantity)
		instance.price = validated_data.get('price', instance.price)
		instance.categories = validated_data.get('categories', instance.categories)
		
		instance.save()
		return instance

	def create(self, validated_data):
		category_data = validated_data.pop('categories')
		product = Product.objects.create(**validated_data)
		dicti={}
		for items in category_data:
			for key, value in items.items() :
				dicti[key] = value
		if 'id' in dicti:
			x= product.categories.get_or_create(id = dicti['id'])
			product.categories.set(x)
		return product


