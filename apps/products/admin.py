from django.contrib import admin

from . import models

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "is_active"]
    list_filter = ["name", "is_active"]
    search_fields = ["name", "slug"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["category", "title", "slug", "is_active", "is_featured"]
    list_filter = ["category", "title", "slug", "is_active", "is_featured"]
    search_fields = ["category", "title", "slug"]


class ProducVarianttAdmin(admin.ModelAdmin):
    list_display = ["material", "sku", "price", "stock"]
    list_filter = ["material", "sku", "price", "stock"]
    search_fields = ["material", "sku"]


class ProducImageAdmin(admin.ModelAdmin):
    list_display = ["product", "alt_text"]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductVariant, ProducVarianttAdmin)
admin.site.register(models.ProductImage, ProducImageAdmin)
