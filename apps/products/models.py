from django.db import models

from apps.core.models import TimeStampModel

# Create your models here.


class Category(TimeStampModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    is_active = models.BooleanField()
