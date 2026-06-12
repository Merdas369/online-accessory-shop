from django.db import models

from apps.core.models import TimeStampModel

# Create your models here.


class Category(TimeStampModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    is_active = models.BooleanField()


class Product(TimeStampModel):
    category = models.ForeignKey(Category, models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField()
    is_featured = models.BooleanField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
