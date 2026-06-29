from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.cart.selectors import cart_selectors
from apps.cart.services.cart_service import Cart


def cart_function(request: HttpRequest):
    cart = request.session.get("cart", {})
    cart_items = cart_selectors.get_cart_items(cart)
    subtotal = cart_selectors.get_cart_subtotal(cart)
    total_vat = cart_selectors.get_cart_vat(cart)
    if request.method == "GET":
        return render(
            request,
            "cart/cart.html",
            {"cart_items": cart_items, "subtotal": subtotal, "total_vat": total_vat},
        )
    if request.method == "POST":
        cart = Cart(request)
        cart.remove_item()
        response = render(
            request,
            "components/cart_badge.html",
            {"cart_items": cart_items, "subtotal": subtotal, "total_vat": total_vat},
        )
        response["HX-Refresh"] = "true"
        return response


def add_to_cart(request):
    if request.method == "POST":
        cart = Cart(request)
        cart.add_item()
    return render(request, "components/success_add.html")


def remove_from_cart(request):
    pass


def update_cart(request):
    return HttpResponse("")
