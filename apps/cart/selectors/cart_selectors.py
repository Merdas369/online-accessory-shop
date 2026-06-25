from decimal import Decimal

from apps.products.models import ProductVariant


def get_cart_items(cart):
    return ProductVariant.objects.filter(pk__in=cart.keys())


def get_cart_count(cart):
    return len(cart)


def get_cart_subtotal(cart):
    subtotal = Decimal(0)
    for variant in ProductVariant.objects.filter(pk__in=cart.keys()):
        subtotal += variant.price
    return subtotal
