from django.db import models
from crunchstore.models.base import BaseUUIDModel
from crunchstore.models.store import Store


class Order(BaseUUIDModel):
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, related_name='orders', null=True)
    order_no = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.IntegerField(default=0)
    payment_id = models.CharField(max_length=50, blank=True, null=True)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    billing_address = models.JSONField(default={})
    customer_details = models.JSONField(default={})

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'orders'
        unique_together = ['store', 'order_no']

    def __str__(self) -> str:
        return self.order_no