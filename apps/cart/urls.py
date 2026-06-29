from django.urls import path

from apps.cart.views import add_to_cart, cart_function, update_cart

urlpatterns = [
    path("", cart_function, name="cart"),
    path("add-to-cart/", add_to_cart, name="add_to_cart"),
    path("update-cart/", update_cart, name="update_cart"),
]
