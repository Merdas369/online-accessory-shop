from django.db import models

from apps.core.models import TimeStampModel

# Create your models here.


class Category(TimeStampModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    is_active = models.BooleanField()


class Product(TimeStampModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField()
    is_featured = models.BooleanField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()


class ProductVariant(models.Model):
    product = models.ManyToManyField(Product)
    material = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField()
