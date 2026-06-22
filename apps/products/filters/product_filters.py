import django_filters

from apps.products.models import Product


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
    )
    ordering = django_filters.OrderingFilter(
        fields=(
            ("title", "title"),
            ("created_at", "created_at"),
            ("min_price", "price"),
        ),
        field_labels={
            "title": "به ترتیب الفبا",
            "created_at": "به ترتیب تاریخ",
            "min_price": "به ترتیب قیمت",
        },
    )

    class Meta:
        model = Product
        fields = []
