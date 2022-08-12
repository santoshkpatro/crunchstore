from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from crunchstore.models.base import BaseUUIDModel
from crunchstore.models.store import Store


class Customer(BaseUUIDModel, AbstractBaseUser):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='customers')
    email = models.EmailField(max_length=255)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_data = models.JSONField(default={})

    password_reset_required = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        db_table = 'customers'
        unique_together = ['store', 'email']

    def __str__(self) -> str:
        return self.full_name