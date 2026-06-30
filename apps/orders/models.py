from django.db import models

from apps.core.models import TimeStampModel


class OrderStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    AWAITING_PAYMENT = "awaiting_payment", "Awaiting_payment"
    PAID = "paid", "Paid"
    FAILED = "failed", "Failed"
    CANCELLED = "cancelled", "Cancelled"
    SHIPPED = "shipped", "Shipped"
    DELIVERED = "delivered", "Delivered"


class Order(TimeStampModel):
    uuid = models.UUIDField()
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    subtotal = models.PositiveIntegerField()
    vat = models.PositiveIntegerField()
    shipping_cost = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
