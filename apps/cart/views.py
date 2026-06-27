from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.cart.services.cart_service import Cart


def cart_function(request: HttpRequest):
    if request.method == "POST":
        cart = Cart(request)
        cart.add_item()
    return render(request, "components/success_add.html")


def add_to_cart(request):
    return HttpResponse("")


def remove_from_cart(request):
    return HttpResponse("")


def update_cart(request):
    return HttpResponse("")
