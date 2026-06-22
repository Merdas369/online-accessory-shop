from django.db.models import Min

from apps.products import models


def get_active_products():
    return (
        models.Product.objects.filter(is_active=True)
        .annotate(min_price=Min("variants__price"))
        .prefetch_related("images", "variants")
    )


def get_featured_products():
    query = models.Product.objects.filter(is_featured=True)
    return list(query)


def get_product_by_slug(slug):
    query = models.Product.objects.filter(slug=slug)
    return list(query)


def get_products_by_category(category):
    query = models.Product.objects.select_related("category").filter(category=category)
    return list(query)
