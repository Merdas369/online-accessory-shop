from django.http import HttpRequest

from apps.products.selectors.category_selector import select_active_category


def navbar_processor(request: HttpRequest):
    return {"navbar_category": select_active_category()}
