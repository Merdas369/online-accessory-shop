from django.db import models


class OrderStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    AWAITING_PAYMENT = "awaiting_payment", "Awaiting_payment"
    PAID = "paid", "Paid"
    FAILED = "failed", "Failed"
    CANCELLED = "cancelled", "Cancelled"
    SHIPPED = "shipped", "Shipped"
    DELIVERED = "delivered", "Delivered"
