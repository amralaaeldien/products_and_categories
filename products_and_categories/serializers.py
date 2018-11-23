from rest_framework import serializers
from products_and_categories.models import Product, Category
from django.db import models

'''class CreatableSlugRelatedField(serializers.SlugRelatedField):
	"""
	Django rest frameork doesn't have a creatble slug field
	so i built one that extends the slug field. it uses djnago
	get_or_create function
	"""
	class Meta:
		model = Category
		fields = ( "name", 'products', 'categories')

	def to_internal_value(self, data):
		try:
			return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
		except models.ObjectDoesNotExist:
			self.fail('does_not_exist', slug_name=self.slug_field,
					value=smart_text(data))
		except (TypeError, ValueError):
			self.fail('invalid')
'''
class CategorySerializer(serializers.ModelSerializer):
	def to_representation(self, obj):
		if 'categories' not in self.fields:
			self.fields['categories'] = CategorySerializer(obj, many=True)      
		return super(CategorySerializer, self).to_representation(obj)

	class Meta:
		model = Category
		fields = ("name", 'products', 'categories')
	
class ProductSerializer(serializers.ModelSerializer):
	categories = CategorySerializer(many=True, required=False)
	'''	categories = CreatableSlugRelatedField(many=False,
											queryset=Category.objects.all(),
											slug_field='categories',
											required=False)
	'''
	class Meta:
		model = Product
		fields = ( "product_code", "name", "quantity", "price", 'categories')

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
		category_data = validated_data.get('categories')
		product = Product.objects.create(**validated_data)
		if category_data:
			for category in category_data:
				product.categories.create(**category)
		return product


