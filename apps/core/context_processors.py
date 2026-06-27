from django.http import HttpRequest

from apps.cart.selectors import cart_selectors
from apps.products.selectors.category_selector import select_active_category


def navbar_processor(request: HttpRequest):
    return {"navbar_category": select_active_category()}


def cart_count_processor(request: HttpRequest):
    return {"cart_count": cart_selectors.get_cart_count(request.session.get("cart", {}))}
