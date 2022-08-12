from django.db import models
from crunchstore.models.base import BaseUUIDModel
from crunchstore.models.product import Product


class ProductResource(BaseUUIDModel):
    TYPE_CHOICES = (
        (0, 'image'),
        (1, 'video'),
        (2, 'pdf')
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='resources')
    type = models.IntegerField(default=0, choices=TYPE_CHOICES)
    resource_data = models.JSONField(default={})

    class Meta:
        db_table = 'product_resources'

    def __str__(self) -> str:
        return str(self.id)

