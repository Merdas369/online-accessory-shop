# Create your views here.

from django.http import HttpRequest
from django.shortcuts import render

from .forms import SearchForm
from .selectors import product_selectors


def product_list(request: HttpRequest):
    if request.method == "GET":
        products = product_selectors.get_active_products()
        return render(request, "products/list.html", {"products": products, "form": SearchForm()})
