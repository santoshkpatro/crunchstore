from django.db import models
from crunchstore.models.base import BaseUUIDModel
from crunchstore.models.store import Store


class Category(BaseUUIDModel):
    store = models.ForeignKey(Store, related_name='catgories', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    thumbnail_data = models.JSONField(default={})

    is_active = models.BooleanField(default=True)


    class Meta:
        db_table = 'catgories'
        unique_together = ['store', 'title']

    def __str__(self) -> str:
        return self.title