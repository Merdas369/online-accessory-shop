from decimal import Decimal

from django.db.models import F

from apps.products.models import ProductVariant


def get_cart_items(cart):
    variants = ProductVariant.objects.filter(pk__in=cart.keys())
    items = []
    for variant in variants:
        items.append(
            {
                "variant": variant,
                "quantity": cart[str(variant.pk)]["quantity"],
            }
        )
    return items


def get_cart_count(cart):
    return len(cart)


def get_cart_subtotal(cart):
    subtotal = Decimal(0)
    for variant in ProductVariant.objects.filter(pk__in=cart.keys()):
        quantity = cart[str(variant.pk)].get("quantity", 0)
        total_price = Decimal(variant.price * quantity)
        subtotal += total_price
    return subtotal


def variant_vat():
    return ProductVariant.objects.all()


def get_cart_vat(cart):
    total_vat = Decimal(0)
    for variant in ProductVariant.objects.filter(pk__in=cart.keys()).annotate(
        vat=(F("price") * Decimal(0.1))
    ):
        quantity = cart[str(variant.pk)].get("quantity", 0)
        vat = Decimal(variant.vat * quantity)
        total_vat += vat
    return round(total_vat, 0)
