from django.db import models

# Create your models here.

class Category(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	categories= models.ManyToManyField('self', related_name='categories', blank=True, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	product_code = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	quantity = models.IntegerField()
	categories = models.ManyToManyField(Category, related_name='products',blank=True)
	
	def __str__(self):
		return self.name

