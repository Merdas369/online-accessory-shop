# Create your views here.

from django.views.generic import ListView

from . import models
from .selectors import product_selectors


class ProductListView(ListView):
    template_name = "products/list.html"
    model = models.Product
    context_object_name = "products"

    def get_queryset(self):
        return product_selectors.get_active_products()
