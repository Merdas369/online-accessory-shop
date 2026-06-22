# Create your views here.

from django.http import HttpRequest
from django.shortcuts import render

from .filters.product_filters import ProductFilter
from .forms import SearchForm
from .selectors import product_selectors


def product_list(request: HttpRequest):
    form = SearchForm(request.GET)
    filter = ProductFilter(request.GET, queryset=product_selectors.get_active_products())

    return render(
        request,
        "products/list.html",
        {"form": form, "filter": filter},
    )
