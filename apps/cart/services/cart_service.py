from django.http import HttpRequest


class Cart:
    def __init__(self, request: HttpRequest) -> None:
        self.request = request

    def add_item(self):
        quantity = int(self.request.POST.get("q", 1))
        variant_id = self.request.POST.get("variant_id", "")

        cart = self.request.session.get("cart", {})

        cart[str(variant_id)] = {
            "quantity": quantity,
        }
        self.request.session["cart"] = cart
        self.request.session.modified = True

    def remove_item(self):
        variant_id = self.request.POST.get("variant_id", "")
        cart = self.request.session.get("cart", {})
        if variant_id in cart:
            cart.pop(variant_id)
            self.request.session["cart"] = cart
            self.request.session.modified = True

    def update_quantity(self):
        quantity = int(self.request.POST.get("q", 1))
        variant_id = self.request.POST.get("variant_id", "")
        cart = self.request.session.get("cart", {})

        if variant_id in cart:
            cart["variant_id"]["quantity"] = quantity
            self.request.session["cart"] = cart
            self.request.session.modified = True
