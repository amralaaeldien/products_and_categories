# Generated by Django 4.1 on 2022-08-08 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_and_categories', '0014_alter_category_name_alter_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories_reversed', to='products_and_categories.category'),
        ),
    ]
