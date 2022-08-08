from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255, unique=True)
	main_category= models.ForeignKey('self', related_name='sub_categories',on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	product_code = models.CharField(max_length=255, unique=True)
	name = models.CharField(max_length=255,blank=True, null=True )
	price = models.IntegerField(blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)
	categories = models.ManyToManyField(Category, related_name='products',blank=True, null=True)
	
	def __str__(self):
		return self.product_code

