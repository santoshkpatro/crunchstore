from django.db import models
from crunchstore.models.base import BaseUUIDModel
from crunchstore.models.store import Store
from crunchstore.models.order import Order
from crunchstore.models.product import Product


class OrderItem(BaseUUIDModel):
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, related_name='store_order_items', null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_meta = models.JSONField(default={})
    quantity = models.PositiveIntegerField(default=1)
    
    class Meta:
        db_table = 'order_items'

    def __str__(self) -> str:
        return str(self.id)