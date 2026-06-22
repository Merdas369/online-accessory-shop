from apps.products.models import Category


def select_active_category():
    return Category.objects.filter(parent__isnull=True, is_active=True).prefetch_related("children")
