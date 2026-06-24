from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list, name="products"),
    path("product/<str:slug>/", views.product_detail, name="product_detail"),
]
