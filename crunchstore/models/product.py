from django.db import models
from crunchstore.models.base import BaseUUIDModel
from crunchstore.models.store import Store
from crunchstore.models.category import Category



class Product(BaseUUIDModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='category_products')
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    available_units = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_free = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
        unique_together = ['store', 'slug']
    
    def __str__(self) -> str:
        return self.title