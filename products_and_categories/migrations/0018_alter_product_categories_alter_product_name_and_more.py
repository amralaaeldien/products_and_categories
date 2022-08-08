# Generated by Django 4.1 on 2022-08-08 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_and_categories', '0017_remove_category_categories_category_main_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='products_and_categories.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]