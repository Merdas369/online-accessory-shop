from django.db import models

from apps.core.models import TimeStampModel

# Create your models here.


class Category(TimeStampModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.is_active}"


class Product(TimeStampModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, db_index=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(db_index=True)
    is_featured = models.BooleanField(db_index=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()

    def __str__(self):
        return self.slug


class ProductVariant(models.Model):
    product = models.ManyToManyField(Product, db_index=True)
    material = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True, db_index=True)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.material} {self.sku}"


class ProductImage(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    alt_text = models.CharField(max_length=255)
    sort_order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.alt_text

    class Meta:
        ordering = ["sort_order"]
