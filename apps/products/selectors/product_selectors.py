from django.db.models import Min

from apps.products import models


def get_active_products():
    return (
        models.Product.objects.filter(is_active=True)
        .annotate(min_price=Min("variants__price"))
        .prefetch_related("images", "variants")
    )


def get_featured_products():
    return models.Product.objects.filter(is_featured=True)


def get_product_by_slug(slug):
    return models.Product.objects.filter(slug=slug).prefetch_related("images", "variants")


def get_products_by_category(category):
    return models.Product.objects.select_related("category").filter(category=category)
