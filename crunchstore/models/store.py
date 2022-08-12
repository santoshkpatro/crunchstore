from django.db import models
from crunchstore.models.base import BaseUUIDModel
from crunchstore.models.user import User


class Store(BaseUUIDModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stores')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    is_open = models.BooleanField(default=True)
    logo_data = models.JSONField(default={})


    class Meta:
        db_table = 'stores'

    def __str__(self) -> str:
        return self.name
