# Create your views here.

from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

from .filters.product_filters import ProductFilter
from .forms import SearchForm
from .selectors import product_selectors


def product_list(request: HttpRequest):
    form = SearchForm(request.GET)
    filter = ProductFilter(request.GET, queryset=product_selectors.get_active_products())
    paginator = Paginator(filter.qs, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    elided_pages = paginator.get_elided_page_range(number=page_obj.number)

    return render(
        request,
        "products/list.html",
        {
            "form": form,
            "filter": filter,
            "elided_pages": elided_pages,
            "page_obj": page_obj,
            "paginator": paginator,
        },
    )


def product_detail(request: HttpRequest, slug):
    product = product_selectors.get_product_by_slug(slug).first()
    return render(request, "products/product_detail.html", {"product": product})
